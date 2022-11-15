from os import environ

# Telegram Bot API
GET_UPDATES_TIMEOUT_SEC = 30

# balcon.exe
PATH_TO_BALCON_EXE = environ.get("PATH_TO_BALCON_EXE")
VOICE = "Microsoft Irina Desktop"
ENCODING = "utf8"
BALCON_EXE_CMD_TEMPLATE = (
    f'{PATH_TO_BALCON_EXE} -n "{VOICE}" -enc {ENCODING}' + ' -f "{input}" -w "{output}"'
)


# lame.exe
PATH_TO_LAME_EXE = environ.get("PATH_TO_LAME_EXE")
LAME_EXE_CMD_TEMPLATE = PATH_TO_LAME_EXE + ' "{input}" "{output}"'
