import os
from tb_message_queue import TbMessageQueue
from tb_message_processor import TbMessageProcessor

"""
- TODO: automated Update-object validation from
    TbAPI getUpdates method
"""

TOKEN = os.environ.get("bot_token")
print(TOKEN)


def main():
    que = TbMessageQueue(TOKEN)
    proc = TbMessageProcessor(TOKEN)
    while True:
        for message in que.get_new_messages():
            proc.process(message)


if __name__ == "__main__":
    main()
