# Telegram convert bot

*an educational project

## Description

The bot is made for converting messages and txt files from a user to mp3.

![pic](https://user-images.githubusercontent.com/8655093/201859016-d614ed04-b331-407e-bd58-acb7bbe6347f.jpg)


## For users
Getting a text which converted in an audio is useful, for example, it's more comfortable to listen an audio than to read some text while walking on the street. Using a bot doesn't require a user to have a converting program on his device.

A user can attach a txt file to the message for the bot in telegram or write a text message.

The bot receives the text and sends an audio back to the user.

## Educational purpose

The project is made for better understanding the work with API, html requests, environmental variables.
Later it's getting to be refactored for the `async` version.

To run a project locally it's needed:
- put token for telegram in .env
- have lame.exe and balcon.exe installed and its paths in .env (works on Windows)
- create a virtual environment (`poetry install` or `python -m venv .venv` and install requirements.txt)
- run `python -m service` 


## Structure

```
service/...
.env                            # environmental variable - token for 
                                # telegram.
.gitignore                      #
config.py                       # paths for programs to convert an audio
convert.py                      # functions to convert files
__main__.py                     # main funcion for running the program
tb_message_processor.py         # checks user's message from telegram
tb_message_queue.py             # checks new messages by calling getUpdates from telebot_api
telebot_api.py                  # requests to api.telegram.org with such 
								# methods as getFile, sendMessage,
								# sendAudio, getUpdates
```
