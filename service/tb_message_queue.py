from service import config as conf
from service.telebot_api import TelebotApi


class TbMessageQueue:
    def __init__(self, token) -> None:
        self.telebot_api = TelebotApi(token)
        self.offset = 0

    async def get_new_messages(self):
        messages = await self.telebot_api.getUpdates(
            offset=self.offset, timeout=conf.GET_UPDATES_TIMEOUT_SEC
        )
        if messages:
            self.offset = messages[-1]["update_id"] + 1

        return messages
