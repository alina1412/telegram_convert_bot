from os import path
from tempfile import TemporaryDirectory

from .convert import convert_txt_to_mp3
from .telebot_api import TelebotApi, TelebotApiFile

# Look also: https://core.telegram.org/bots/api#message


class TbMessageProcessor:
    def __init__(self, token) -> None:
        self.telebot_api = TelebotApi(token)

    def process(self, message):
        self.process_text(message)
        self.process_file(message)

    def process_text(self, message):
        if not ("message" in message and "text" in message["message"]):
            return
        text = message["message"]["text"]
        chat_id = message["message"]["from"]["id"]
        answer = (
            "Попытаюсь прислать ваше сообщение в виде аудио. "
            + "Ещё можно присылать txt"
        )
        self.telebot_api.sendMessage(text=answer, chat_id=chat_id)

        with TemporaryDirectory(prefix="telebot_") as tmpdirname:
            document_path = tmpdirname + r"\text.txt"
            self.save_to_txt(text, document_path)
            self.prepare_and_send_mp3(document_path, chat_id)

    def process_file(self, message):
        if not ("message" in message and "document" in message["message"]):
            return
        doc = message["message"]["document"]
        chat_id = message["message"]["from"]["id"]

        with TemporaryDirectory(prefix="telebot_") as tmpdirname:
            document_path = self.telebot_api.download_document(doc, tmpdirname)
            self.prepare_and_send_mp3(document_path, chat_id)

    def save_to_txt(self, text, document_path):
        with open(document_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(text)
        # print("does exist -- ", os.path.exists(document_path))

    def prepare_and_send_mp3(self, document_path, chat_id):
        document_path_mp3 = path.splitext(document_path)[0] + ".mp3"
        try:
            convert_txt_to_mp3(document_path, document_path_mp3)
        except Exception as ex:
            print(ex)
            return

        with open(document_path_mp3, "rb") as mp3_file:
            tb_file = TelebotApiFile(
                name=path.basename(document_path_mp3),
                file=mp3_file,
                media_type="audio/mpeg",
            )
            self.telebot_api.sendAudio(chat_id=chat_id, audio=tb_file)
