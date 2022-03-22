
from tempfile import TemporaryDirectory
import os
from telebot_api import TelebotApi, TelebotApiFile
from convert import convert_txt_to_mp3

# Look also: https://core.telegram.org/bots/api#message


class TbMessageProcessor:
    def __init__(self, token) -> None:
        self.telebot_api = TelebotApi(token)

    def process(self, message):
        self.process_echo(message)
        self.process_file(message)

    def process_echo(self, message):
        if "message" in message:
            if "text" in message["message"]:
                text = message['message']['text']
                chat_id = message['message']['from']['id']
                self.telebot_api.sendMessage(text=text, chat_id=chat_id)

    def process_file(self, message):
        if "message" in message and 'document' in message['message']:
            doc = message['message']['document']
            chat_id = message['message']['from']['id']

            with TemporaryDirectory(prefix="telebot_") as tmpdirname:
                document_path = self.telebot_api.download_document(
                    doc, tmpdirname)
                document_path_mp3 = os.path.splitext(document_path)[0] + ".mp3"

                if convert_txt_to_mp3(document_path, document_path_mp3):
                    with open(document_path_mp3, "rb") as mp3_file:
                        tb_file = TelebotApiFile(
                            name=os.path.basename(document_path_mp3),
                            file=mp3_file,
                            media_type="audio/mpeg",
                        )
                        self.telebot_api.sendAudio(
                            chat_id=chat_id,
                            audio=tb_file
                        )
