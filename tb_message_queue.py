from telebot_api import TelebotApi
import config as conf


class TbMessageQueue:
    def __init__(self, token) -> None:
        self.telebot_api = TelebotApi(token)
        self.offset = 0

    def get_new_messages(self):
        messages = self.telebot_api.getUpdates(
            offset=self.offset, timeout=conf.GET_UPDATES_TIMEOUT_SEC)
        if messages:
            self.offset = messages[-1]["update_id"] + 1

        return messages
