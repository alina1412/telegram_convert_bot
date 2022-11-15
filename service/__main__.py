import asyncio
from os import environ
from .tb_message_queue import TbMessageQueue
from .tb_message_processor import TbMessageProcessor


TOKEN = environ.get("bot_token")
# print(TOKEN)


async def main():
    que = TbMessageQueue(TOKEN)
    proc = TbMessageProcessor(TOKEN)
    while True:
        for message in await que.get_new_messages():
            await proc.process(message)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        print("started...")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("wait...")
        pass
