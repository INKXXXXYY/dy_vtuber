import os
import random

# AUDIO_DIR = 'wav\\guide_wav'
# TRACKING_FILE = 'selected_audios.txt'

def get_random_audio(AUDIO_DIR,TRACKING_FILE):
    # 获取所有的音频文件
    all_audios = [f for f in os.listdir(AUDIO_DIR) if f.endswith('.wav')]
    
    # 检查已经选择的音频
    if os.path.exists(TRACKING_FILE):
        with open(TRACKING_FILE, 'r') as f:
            selected_audios = f.read().splitlines()
    else:
        selected_audios = []
    
    # 获取未被选择的音频
    unselected_audios = [audio for audio in all_audios if audio not in selected_audios]
    
    # 如果所有音频都已经被选择，重置跟踪文件
    if not unselected_audios:
        os.remove(TRACKING_FILE)
        unselected_audios = all_audios

    # 随机选择一个未被选择的音频
    chosen_audio = random.choice(unselected_audios)

    # 更新跟踪文件
    with open(TRACKING_FILE, 'a') as f:
        f.write(chosen_audio + '\n')

    return os.path.join(AUDIO_DIR, chosen_audio)

# # 使用示例
# audio_path = get_random_audio()
# print(f"Chosen audio: {audio_path}")
