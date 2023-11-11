import requests
import os
import random
import string
import time
from pydub import AudioSegment
from pydub.playback import play
import winsound
import threading

play_lock = threading.Lock()

# 生成一个随机的文件名
def generate_random_filename(length=10):
    characters = string.ascii_letters + string.digits
    random_chars = ''.join(random.choice(characters) for _ in range(length))
    timestamp = int(time.time())
    return f"{random_chars}_{timestamp}.wav"

# 异步播放WAV文件的函数
def async_play_wav_windows(file_path):
    def play():
        with play_lock:
            print(file_path)
            winsound.PlaySound(file_path, winsound.SND_FILENAME)
    thread = threading.Thread(target=play)
    thread.start()

# 请求并保存WAV文件的函数
def request_and_save_wav(text, lang, id=1,output_directory="./audio/"):
    api_url = "http://192.168.31.112:23456/voice/bert-vits2"
    data = {"text": text, "lang": lang,"id": id}
    response = requests.post(api_url, data=data)

    if response.status_code == 200:
        output_file = os.path.join(output_directory, generate_random_filename())
        with open(output_file, "wb") as wav_file:
            wav_file.write(response.content)

        # 处理音频文件，增大音量
        amplify_audio_and_add_silence(output_file)

        print(f"Wav文件已保存为 {output_file}")
        return output_file
    else:
        print(f"请求失败，状态码: {response.status_code}")


# 增大音频文件音量并在末尾添加静音的函数
def amplify_audio_and_add_silence(file_path, volume_increase=12, silence_duration=2000):  # 静音持续2000毫秒（2秒）
    audio = AudioSegment.from_wav(file_path)
    louder_audio = audio + volume_increase
    silence = AudioSegment.silent(duration=silence_duration)

    # 将静音添加到音频末尾
    final_audio = louder_audio + silence

    final_audio.export(file_path, format="wav")

# Windows平台上播放WAV文件的函数
def play_wav_windows(file_path):
    winsound.PlaySound(file_path, winsound.SND_FILENAME)

# 播放WAV文件的函数
def play_wav(file_path):
    audio = AudioSegment.from_wav(file_path)
    play(audio)

# 修改pydub的转换器路径，如果需要
# AudioSegment.converter = "/path/to/ffmpeg"
