# import vlc
# import time

# def play_video_with_sound(video_path, x_pos=0, y_pos=0):
#     # 创建一个VLC实例
#     instance = vlc.Instance()

#     # 创建一个MediaPlayer对象
#     player = instance.media_player_new()

#     # 设置media
#     media = instance.media_new(video_path)
#     player.set_media(media)

#     # 设置窗口位置
#     # player.set_x(x_pos)
#     # player.set_y(y_pos)

#     # 播放视频
#     player.play()

#     # 让视频播放，直到结束
#     time.sleep(media.get_duration() / 1000)

#     player.stop()


# import vlc
# import time
# import pygetwindow as gw
# import pyautogui

# def play_video_with_sound(video_path, x_pos=0, y_pos=0):
#     # 创建一个VLC实例
#     instance = vlc.Instance()

#     # 创建一个MediaPlayer对象
#     player = instance.media_player_new()

#     # 设置media
#     media = instance.media_new(video_path)
#     player.set_media(media)

#     # 播放视频
#     player.play()
    
#     # 稍等一下以确保窗口已打开
#     time.sleep(2)
    
#     # 查找VLC窗口并设置其位置
#     vlc_windows = [window for window in gw.getWindowsWithTitle('') if 'VLC media player' in window.title]
#     if vlc_windows:
#         pyautogui.moveTo(vlc_windows[0]._hWnd, x_pos, y_pos)
    
#     # 让视频播放，直到结束
#     time.sleep(media.get_duration() / 1000)

#     player.stop()



import vlc
import time
import pygetwindow as gw
import pyautogui

# def play_video_with_sound(video_path, x_pos=0, y_pos=0):
#     # 创建一个VLC实例
#     instance = vlc.Instance()

#     # 创建一个MediaPlayer对象
#     player = instance.media_player_new()

#     # 设置media
#     media = instance.media_new(video_path)
#     player.set_media(media)

#     # 播放视频
#     player.play()
    
#     # 稍等一下以确保窗口已打开
#     time.sleep(2)
    
#     # 查找VLC窗口并设置其位置
#     vlc_windows = [window for window in gw.getWindowsWithTitle('') if 'VLC media player' in window.title]
#     if vlc_windows:
#         # 这里使用pyautogui的moveRel，它基于当前窗口的位置来移动窗口。
#         # 先将窗口移到屏幕的0,0位置，然后移动到目标位置
#         pyautogui.moveTo(vlc_windows[0]._hWnd, 0, 0)
#         pyautogui.moveRel(x_pos, y_pos)
    
#     # 让视频播放，直到结束
#     time.sleep(media.get_duration() / 1000)

#     player.stop()


import vlc
import time
import pygetwindow as gw
import pyautogui

pyautogui.FAILSAFE = False


def play_video_with_sound(video_path, x_pos=0, y_pos=0):

    # 创建一个VLC实例
    instance = vlc.Instance()

    # 创建一个MediaPlayer对象
    player = instance.media_player_new()

    # 设置media
    media = instance.media_new(video_path)
    player.set_media(media)

    # 播放视频
    player.play()

    # 稍等一下以确保窗口已打开
    time.sleep(0.3)

    # 查找VLC窗口并设置其位置
    # vlc_windows = [window for window in gw.getWindowsWithTitle('') if 'VLC (Direct3D11 output)' in window.title]
    # if vlc_windows:
    #     # 这里使用pyautogui的moveRel，它基于当前窗口的位置来移动窗口。
    #     # 先将窗口移到屏幕的0,0位置，然后移动到目标位置``
    #     pyautogui.moveTo(vlc_windows[0]._hWnd, -1024, 932)
    #     pyautogui.moveRel(x_pos, y_pos)
    
    # 示例：将VLC窗口移动到屏幕的(100, 100)位置
    move_vlc_window(-1000, 100)

    # 检查视频是否播放完毕
    while player.get_state() != vlc.State.Ended:
        time.sleep(1)  # 每秒检查一次

    player.stop()


import pygetwindow as gw
import pyautogui

def move_vlc_window(x, y):
    # 获取名为"VLC (Direct3D11 output)"的窗口
    vlc_windows = gw.getWindowsWithTitle("VLC (Direct3D11 output)")
    if vlc_windows:
        vlc_window = vlc_windows[0]  # 获取第一个找到的VLC窗口
        vlc_window.moveTo(x, y)      # 移动窗口到指定位置
    else:
        print("VLC window not found!")




# 假设拓展屏的宽度是1920像素，将VLC放在扩展屏的最左边
# play_video_with_sound("path_to_your_video.mp4", x_pos=-1920, y_pos=0)
