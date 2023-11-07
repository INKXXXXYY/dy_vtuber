import threading
import queue

# from voice_in import request_and_save_wav

def request_and_save(part, request_func, q):
    path = request_func(part, "zh")
    q.put(path)

def play_sequentially_with_preloading(parts, request_func, play_func):
    """
    按顺序播放视频，同时预加载下一个视频

    :param parts: 要处理和播放的部分列表
    :param request_func: 请求并保存视频的函数
    :param play_func: 播放视频的函数
    """
    # 创建一个队列来存储请求的视频路径
    video_queue = queue.Queue()

    # 请求第一段视频
    video_queue.put(request_func(parts[0], "zh"))

    for i in range(1, len(parts)):
        # 从队列中获取上一个视频的路径，并播放
        video_path = video_queue.get()
        play_func(video_path)

        # 在播放上一个视频的同时，启动线程请求下一个视频
        thread = threading.Thread(target=request_and_save, args=(parts[i], request_func, video_queue))
        thread.start()

        # 为了确保主线程等待最后一个视频请求完成
        if i == len(parts) - 1:
            thread.join()

    # 播放最后一段视频
    video_path = video_queue.get()
    play_func(video_path)

# 使用方法：
# play_sequentially_with_preloading(parts, request_and_save_wav, play_video_with_sound)
