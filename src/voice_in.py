import requests
import os
import random
import string
import time

def generate_random_filename(length=10):
    # 生成一个随机的文件名
    characters = string.ascii_letters + string.digits
    random_chars = ''.join(random.choice(characters) for _ in range(length))
    timestamp = int(time.time())
    return f"{random_chars}_{timestamp}.mp4"

import winsound
import threading

play_lock = threading.Lock()

def async_play_wav_windows(file_path):
    """
    异步播放WAV文件，使用线程，确保同一时间只有一个音频在播放。
    """
    def play():
        with play_lock:
            winsound.PlaySound(file_path, winsound.SND_FILENAME)

    thread = threading.Thread(target=play)
    thread.start()

def request_and_save_wav(text, lang, output_directory="./audio/"):
    # 定义API的URL
    api_url = "http://region-31.seetacloud.com:57975/voice/bert-vits2"

    # 定义要发送的参数
    data = {
        "text": text,
        "lang": lang,
    }

    # 发送POST请求
    response = requests.post(api_url, data=data)

    # 检查响应状态码
    if response.status_code == 200:
        # 生成一个随机的文件名
        output_file = os.path.join(output_directory, generate_random_filename())

        # # 将响应内容保存为 MP4 文件
        # with open(output_file, "wb") as mp4_file:
        #     mp4_file.write(response.content)

        # # 将响应内容保存为 WAV 文件
        # with open(output_file, "wb") as wav_file:
        #     wav_file.write(response.content)

        # print(f"Wav文件已保存为 {output_file}")
            # 将响应内容保存为 WAV 文件
        with open(output_file, "wb") as wav_file:
            wav_file.write(response.content)

        # 加入2秒的静音
        audio = AudioSegment.from_wav(output_file)
        silence = AudioSegment.silent(duration=2000)  # 2秒的静音
        extended_audio = audio + silence
        extended_audio.export(output_file, format="wav")

        print(f"Wav文件已保存为 {output_file}")
        return output_file

        # 播放保存的WAV文件
        # play_wav(output_file)
        # play_wav_windows(output_file)
        

        print(f"Wav文件已保存为 {output_file}")
        return output_file
    else:
        print(f"请求失败，状态码: {response.status_code}")

from pydub import AudioSegment
from pydub.playback import play
AudioSegment.converter = "/"

import winsound

def play_wav_windows(file_path):
    winsound.PlaySound(file_path, winsound.SND_FILENAME)


def play_wav(file_path):
    """播放指定的WAV文件"""
    audio = AudioSegment.from_wav(file_path)
    play(audio)