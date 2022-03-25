# Telegram convert bot

## Description

The bot is made for converting messages and txt files from a user to mp3.

Sometimes it's more comfortable to listen an audio than to read some text, for example, while walking on the street. Getting a converted audio is useful, and it doesn't require a user to have a converting program on his device.

## Usage

A user can attach a `txt` file to the message for the bot in telegram or write a text message.

The bot receives the text and sends an audio back to the user.

## Why this project is made?

The purposes of making the project were: educational one for better understanding the work with API, html requests, environmental variables.

## Structure

```py
.env.example                    # environmental variable - token for 
                                # telegram.
.gitignore                      #
config.py                       # paths for programs to convert an audio
convert.py                      # functions to convert files
program.py                      # main funcion for running the program
tb_message_processor.py         # checks user's message from telegram
tb_message_queue.py             # checks new messages by calling getUpdates from telebot_api
telebot_api.py                  # requests to api.telegram.org with such 
								# methods as getFile, sendMessage,
								# sendAudio, getUpdates
```
