import subprocess
import os

import config as conf


def convert_txt_to_wav(in_file_address, out_file_address) -> bool:
    if not os.path.exists(in_file_address):
        print('convert_to_wav: file not exists')
        return False

    command_line = conf.BALCON_EXE_CMD_TEMPLATE.format(
        input=in_file_address,
        output=out_file_address,
    )

    subprocess.call(command_line)
    if os.path.exists(out_file_address):
        print("out_file_address: ", out_file_address)
        print('converted to wav')
        return True
    return False


def convert_wav_to_mp3(in_file_address, out_file_address) -> bool:
    command_line = conf.LAME_EXE_CMD_TEMPLATE.format(
        input=in_file_address,
        output=out_file_address,
    )

    subprocess.call(command_line)
    if os.path.exists(out_file_address):
        print('converted to mp3')
        return True
    return False


def convert_txt_to_mp3(in_file_address, out_file_address) -> bool:
    out_wav = out_file_address + ".wav"
    if convert_txt_to_wav(in_file_address, out_wav):
        if convert_wav_to_mp3(out_wav, out_file_address):
            os.remove(out_wav)
            return True
    return False
