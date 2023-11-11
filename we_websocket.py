import datetime
import os
import queue
import threading
import time
# from request_save import play_sequentially_with_preloading
import websocket
import json
# from src.play import play_video_with_sound
from src.recieve_guide import extract_content
# from request_save import play_sequentially_with_preloading
# from src.process_tarot_question import process_tarot_question
# from tarot_easy import is_tarot_question,parse_answer,tarot_answer, transform_text
from utils.get_random_audio import get_random_audio
from src.voice_in import async_play_wav_windows, play_wav_windows, request_and_save_wav
# from wav_infer import run_inference_command

# 创建一个线程安全的队列
message_queue = queue.Queue()

# 添加一个变量来保存上次消息的时间
last_message_time = datetime.datetime.now()

WARM_UP_INTERVAL = 300  # 例如，300s无消息就播放暖场音频
WARM_UP_AUDIO = 'wav\\introduce.wav'  # 暖场音频的文件路径

def warm_up_worker():
    """检查最后一次消息的时间，并在必要时播放暖场音频。"""
    global last_message_time
    while True:
        time.sleep(5)  # 每10秒检查一次
        if (datetime.datetime.now() - last_message_time).total_seconds() > WARM_UP_INTERVAL:
            print("播放暖场音频")
            async_play_wav_windows(WARM_UP_AUDIO)
            last_message_time = datetime.datetime.now()  # 更新时间戳，避免连续播放


# 启动暖场工作线程
# warm_up_thread = threading.Thread(target=warm_up_worker)
# warm_up_thread.start()

# 播放音频的函数
def play_fixed_audio_periodically():
    global last_message_time

    while True:
        # 等待十五分钟
        # time.sleep(150)
        # 获取固定音频路径
        # wav_data_PATH = "固定音频路径.wav"
        # 输出固定guide音频
        time.sleep(5)  # 每10秒检查一次

        if (datetime.datetime.now() - last_message_time).total_seconds() > 150:

            AUDIO_DIR = 'wav\\juben'
            TRACKING_FILE = 'utils\\selected_audios1.txt'
            print("播放剧本")
            wav_data_PATH=get_random_audio(AUDIO_DIR,TRACKING_FILE)
            async_play_wav_windows(wav_data_PATH)
            last_message_time = datetime.datetime.now()  # 更新时间戳，避免连续播放

            # 播放音频
            # async_play_wav_windows(wav_data_PATH)



# 创建并启动线程
# audio_thread = threading.Thread(target=play_fixed_audio_periodically)
# audio_thread.start()


def play_geng_fixed_audio_periodically():
    global last_message_time

    while True:
        # 等待十五分钟
        # time.sleep(60)
        # 获取固定音频路径
        # wav_data_PATH = "固定音频路径.wav"
        # 输出固定guide音频
        time.sleep(5)  # 每10秒检查一次
        if (datetime.datetime.now() - last_message_time).total_seconds() > 30:
            AUDIO_DIR = 'wav\\geng'
            TRACKING_FILE = 'utils\\selected_audios2.txt'
            print("播放geng")
            wav_data_PATH = get_random_audio(AUDIO_DIR, TRACKING_FILE)
            async_play_wav_windows(wav_data_PATH)
            last_message_time = datetime.datetime.now()  # 更新时间戳，避免连续播放


        # 播放音频
        # async_play_wav_windows(wav_data_PATH)


# 创建并启动线程
# audio_thread = threading.Thread(target=play_geng_fixed_audio_periodically)
# audio_thread.start()

def worker():
    """从队列中获取并处理消息的工作线程函数。"""
    while True:
        message = message_queue.get()  # 从队列中获取消息
        if message is None:  # 如果收到 None，工作线程就会结束
            break
        handle_message(message)  # 处理消息
        message_queue.task_done()

# 启动工作线程
t = threading.Thread(target=worker)
t.start()


# 定义全局变量
global last_welcome_time
last_welcome_time = None
global welcome_counter
welcome_counter = 0

def handle_message(message):
    """处理弹幕的函数。"""
    # 这里是您原来在 on_message 中的处理逻辑
    # ...
    global last_message_time  # 使用全局变量
    last_message_time = datetime.datetime.now()  # 更新最后消息的时间


    try:
        received_data = json.loads(message)
        
        # 检查 'Type' 是否为 1（弹幕）
        if received_data.get('Type') == 1:

            # 处理弹幕进行反馈
            content=extract_content(received_data)

        # 检查 'Type' 是否为 3（进入直播间）
        elif received_data.get('Type') == 3:
            pass

            # global last_welcome_time
            # global welcome_counter
            #
            # # 获取当前时间
            # current_time = datetime.datetime.now()
            #
            # # 如果是第一个人或上一个欢迎时间距离现在超过一分钟，欢迎新观众
            # if welcome_counter < 2 or (last_welcome_time and (current_time - last_welcome_time).total_seconds() > 60):
            #     welcome_content = "，来了"
            #     data_dict = json.loads(received_data['Data'])
            #     nickname = data_dict['User']['Nickname']
            #     print("正在执行音频转换请求")
            #     wav_data_PATH = request_and_save_wav("亲爱的" + nickname + welcome_content, "zh")
            #     async_play_wav_windows(wav_data_PATH)
            #
            #     # 更新欢迎时间和计数器
            #     last_welcome_time = current_time
            #     welcome_counter += 1


    except json.JSONDecodeError:
        print("Error decoding JSON")
    except TypeError as e:
        print("TypeError:", e)
    except KeyError as e:
        print("KeyError:", e)


# 定义当接收到消息时的回调函数
def on_message(ws, message):
    message_queue.put(message)



# 定义当连接发生错误时的回调函数
def on_error(ws, error):
    print("Error:", error)

# 定义当连接关闭时的回调函数
def on_close(ws, close_status_code, close_msg):
    print("Closed:", close_status_code, close_msg)

# 定义当连接成功打开时的回调函数
def on_open(ws):
    print("Connection opened")


# 创建 WebSocket 连接
ws = websocket.WebSocketApp("ws://127.0.0.1:8888/",  # 替换为您的 WebSocket 服务地址
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)
ws.on_open = on_open
ws.run_forever()
