#

# Telegram Bot API
GET_UPDATES_TIMEOUT_SEC = 30

# balcon.exe
PATH_TO_BALCON_EXE = r"C:\Distr\balcon\balcon.exe"
# PATH_TO_BALCON_EXE = r"C:\Users\sentenzo\Downloads\balcon\balcon.exe"
VOICE = "Microsoft Irina Desktop"
ENCODING = "utf8"
BALCON_EXE_CMD_TEMPLATE = (
    f'{PATH_TO_BALCON_EXE} -n "{VOICE}" -enc {ENCODING}' +
    ' -f "{input}" -w "{output}"'
)

# C:\Users\sentenzo\Downloads\balcon\balcon.exe -n "Microsoft Irina Desktop" -f "C:\Users\sentenzo\AppData\Local\Temp\telebot_qzeb3a32\New Text Document.txt" -w "C:\Users\sentenzo\AppData\Local\Temp\telebot_qzeb3a32\New Text Document.mp3.wav" # noqa: E501

# lame.exe
PATH_TO_LAME_EXE = r"C:\Distr\balabolka\utils\lame.exe"
# PATH_TO_LAME_EXE = r"C:\Users\sentenzo\Downloads\Balabolka\utils\lame.exe"
LAME_EXE_CMD_TEMPLATE = PATH_TO_LAME_EXE + " \"{input}\" \"{output}\""
