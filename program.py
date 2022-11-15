from os import environ
from service.tb_message_queue import TbMessageQueue
from service.tb_message_processor import TbMessageProcessor


TOKEN = environ.get("bot_token")
# print(TOKEN)


def main():
    que = TbMessageQueue(TOKEN)
    proc = TbMessageProcessor(TOKEN)
    while True:
        for message in que.get_new_messages():
            proc.process(message)


if __name__ == "__main__":
    main()
