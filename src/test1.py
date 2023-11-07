import time
import requests

from utils.get_random_audio import get_random_audio
from src.voice_in import async_play_wav_windows, request_and_save_wav

group_id="1688987355385794"
api_key="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJOYW1lIjoidGFyb3RfYWdlbnQiLCJTdWJqZWN0SUQiOiIxNjg4OTg3MzU1ODUwODM2IiwiUGhvbmUiOiJNVGd3TWpVMk1qQXhORGM9IiwiR3JvdXBJRCI6IjE2ODg5ODczNTUzODU3OTQiLCJQYWdlTmFtZSI6IiIsIk1haWwiOiJwbUB2YW5nZW5nLmNvbSIsIkNyZWF0ZVRpbWUiOiIyMDIzLTEwLTMxIDExOjExOjA3IiwiaXNzIjoibWluaW1heCJ9.dlfFfSWnzaFas4-hLh0wU7_JEop9mV7J9D9gC6sJMiBqF119Dl7TXnPzK8hs8TN09_9ZVHF0VVW4zhFTmsbKeqkjhqt-WDp8ewZfZiZK3J-lpGccPEFT1o4eCkMHeB4ODyafgn6F4r3BQ5K7_oLSWInMG4OW50L-AswCUWmwHExKQMuAMhLb1r0KcZxuru779tOrG_hvTYN1DMEhmglZbb5yQPHa9Ru23EHqgX88otbLs0z9hD4z_f0JuGz9BRudnKqPaC2KwKWte7Dm24UQHJuv4SsZVootDXC9SFaSlkehFZqqQDSK6raUbBiE7_3TdvkNIfouCjLZ3QHc67HCbA"

url = "https://api.minimax.chat/v1/text/chatcompletion_pro?GroupId=" + group_id

payload = {
    "bot_setting": [
        {
            "bot_name": "塔罗占卜师",
            "content": "你现在是塔罗占卜师的助理，请你判断该问题是否属于塔罗占卜师可以回答的问题，如果不是，则回复 \"NO\"，是则回复 \"YES\"，使用 json 的公式，如下：\n{\"answer\":\"YES\"}"
        }
    ],
    "messages": [{"sender_type": "USER", "sender_name": "小明", "text": "请问今天天气怎么样"}],

    "reply_constraints": {"sender_type": "BOT", "sender_name": "塔罗占卜师"},
    "model": "abab5.5-chat",
    "tokens_to_generate": 1034,
    "temperature": 0.01,
    "top_p": 0.95,
}
headers = {"Content-Type": "application/json", "Authorization": "Bearer " + api_key}

response = requests.request("POST", url, headers=headers, json=payload)

print(response.status_code)
print(response.text)


import json
import os
import random
import requests
# from flask import Flask, app, jsonify, request

group_id = "1688987355385794"

# api_key = "YOUR_API_KEY" # Do not expose API keys in source code; this is a security risk.
api_key = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJOYW1lIjoidGFyb3RfYWdlbnQiLCJTdWJqZWN0SUQiOiIxNjg4OTg3MzU1ODUwODM2IiwiUGhvbmUiOiJNVGd3TWpVMk1qQXhORGM9IiwiR3JvdXBJRCI6IjE2ODg5ODczNTUzODU3OTQiLCJQYWdlTmFtZSI6IiIsIk1haWwiOiJwbUB2YW5nZW5nLmNvbSIsIkNyZWF0ZVRpbWUiOiIyMDIzLTEwLTMxIDExOjExOjA3IiwiaXNzIjoibWluaW1heCJ9.dlfFfSWnzaFas4-hLh0wU7_JEop9mV7J9D9gC6sJMiBqF119Dl7TXnPzK8hs8TN09_9ZVHF0VVW4zhFTmsbKeqkjhqt-WDp8ewZfZiZK3J-lpGccPEFT1o4eCkMHeB4ODyafgn6F4r3BQ5K7_oLSWInMG4OW50L-AswCUWmwHExKQMuAMhLb1r0KcZxuru779tOrG_hvTYN1DMEhmglZbb5yQPHa9Ru23EHqgX88otbLs0z9hD4z_f0JuGz9BRudnKqPaC2KwKWte7Dm24UQHJuv4SsZVootDXC9SFaSlkehFZqqQDSK6raUbBiE7_3TdvkNIfouCjLZ3QHc67HCbA"

url = "https://api.minimax.chat/v1/text/chatcompletion_pro?GroupId=" + group_id

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

def tarot_answer(user_question, intend, cards, bot_name="塔罗占卜师"):
    cards_text = '\n'.join([f"{i+1}. {card}" for i, card in enumerate(cards)])
    content_template = """
你是一个直播间的主播，现在直播的内容是塔罗占卜，请根据抽中的牌回答用户的提问。
回答问题时，请始终给出积极的答案，如果对于荒诞的问题，根据牌面结合用户意图给出积极的答案；

回答问题时，按照以下顺序：
1. 复述抽中的牌面和正逆位情况
2. 作出分析
    """
    # ===
    # 抽中的牌如下：
    # {cards}
    # 用户意图：{intend}
    # ===

    content = content_template.format(cards=cards_text, intend=intend)
    content2 = "{\"question\":\"" + user_question + "\"}"

    payload = {
        "bot_setting": [
            {
                "bot_name": "塔罗占卜师",
                "content":content
                # "content": "你现在是塔罗占卜师的助理，请你判断该问题是否属于占卜师可以回答的问题，如果不是，则回复 \"NO\"，是则回复 \"YES\"，使用 json 的公式，如下：\n{\"answer\":\"YES\"}"
            }
        ],
        "messages": [{"sender_type": "USER", "sender_name": "小明", "text": content2}],
        "reply_constraints": {"sender_type": "BOT", "sender_name": "塔罗占卜师"},
        "model": "abab5.5-chat",
        "tokens_to_generate": 1034,
        "temperature": 0.01,
        "top_p": 0.95,
    }

    # url = "https://api.minimax.chat/v1/text/chatcompletion_pro?GroupId=" + group_id
    # headers = {"Content-Type": "application/json", "Authorization": "Bearer " + api_key}

    headers = {"Content-Type": "application/json", "Authorization": "Bearer " + api_key}

    response = requests.request("POST", url, headers=headers, json=payload)


    response = requests.post(url, headers=headers, json=payload)
    response_json = response.json()
    
    return response_json["choices"][0]["messages"][0]["text"]


def is_tarot_question(user_name,user_content):
    payload = {
        "bot_setting": [
            {
                "bot_name": "塔罗占卜师",
                "content": "你现在是塔罗占卜师的助理，请你判断该问题是否属于塔罗可以占卜的问题，如果不是，则回复 \"NO\"，是则回复 \"YES\"，使用 json 的公式，如下：\n{\"answer\":\"YES\"}"
            }
        ],
        "messages": [{"sender_type": "USER", "sender_name": user_name, "text": user_content}],
        "reply_constraints": {"sender_type": "BOT", "sender_name": "塔罗占卜师"},
        "model": "abab5.5-chat",
        "tokens_to_generate": 1034,
        "temperature": 0.01,
        "top_p": 0.95,
    }
    
    response = requests.post(url, headers=headers, json=payload).json()
    # answer_text = response["choices"][0]["messages"][0]["text"]
    print(response)

    answer = response["reply"]
    print("answer: ",answer)
    print("----------------------------")
    return answer

# ... [rest of your functions remain as they are] ...

def parse_answer(answer):
    try:
        parsed_data = json.loads(answer)

        # print(answer)
        final=parsed_data["answer"]
        print('answer_test', final)
        if final == 'NO':
            print('parse_answer not ok')
            return '0'
        elif final == 'YES':
            print('parse_answer ok')
            return '1'
        else:
            print('parse_answer error')
            return "error"
    except json.JSONDecodeError:
        return "error"

def draw_random_cards_with_orientation(json_file_path, num_cards=3):
    """
    从指定的 JSON 文件中随机抽取指定数量的卡片，并随机赋予正逆位。
    
    参数:
    - json_file_path (str): JSON 文件的路径
    - num_cards (int): 要抽取的卡片数量

    返回:
    - random_cards_json (str): 随机抽取并赋予正逆位的卡片（JSON 格式）
    """
    # 从文件中加载卡片列表
    with open(json_file_path, 'r', encoding='utf-8') as f:
        tarot_cards = json.load(f)
    
    # 随机抽取卡片
    random_cards = random.sample(tarot_cards, num_cards)
    
    # 随机赋予正逆位
    orientations = ["正位", "逆位"]
    random_cards_with_orientation = [f"{card}（{random.choice(orientations)}）" for card in random_cards]
    
    # 转换为 JSON 格式
    random_cards_json = json.dumps(random_cards_with_orientation, ensure_ascii=False)
    
    return random_cards_json

def num_to_chinese(num_str: str) -> str:
    digits = {
        '0': '零',
        '1': '一',
        '2': '二',
        '3': '三',
        '4': '四',
        '5': '五',
        '6': '六',
        '7': '七',
        '8': '八',
        '9': '九'
    }
    units = ['', '十', '百', '千']
    
    if not num_str.isdigit():
        return num_str
    
    num_len = len(num_str)
    if num_len > 4:
        return num_str  # 如果数字超过4位，不转换

    result = ''
    zero_flag = False
    for idx, char in enumerate(num_str):
        if char == '0':
            zero_flag = True
        else:
            if zero_flag:
                result += digits['0']
                zero_flag = False
            result += digits[char] + units[num_len - idx - 1]
    return result

def transform_text(text: str) -> str:
    import re
    
    # 将逗号、句号、感叹号替换为 |
    text = text.replace('，', '|').replace('。', '|').replace('！', '|')
    
    # 移除括号和引号
    remove_chars = ['「', '」', '“', '”', '(', ')', '[', ']', '{', '}', '"', "'"]
    for char in remove_chars:
        text = text.replace(char, '')
    
    # 使用正则替换所有阿拉伯数字为中文数字
    text = re.sub(r'\d+', lambda m: num_to_chinese(m.group()), text)
    
    return text


def get_emotional_intent(user_input):
    """
    输入用户问题，返回用户意图，如果识别为非意图，则返回{"answer":"NO"}

    Args:
        user_input (str): 用户输入的问题

    Returns:
        str: json 格式
    """
    
    group_id = "1688987355385794"
    api_key = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJOYW1lIjoidGFyb3RfYWdlbnQiLCJTdWJqZWN0SUQiOiIxNjg4OTg3MzU1ODUwODM2IiwiUGhvbmUiOiJNVGd3TWpVMk1qQXhORGM9IiwiR3JvdXBJRCI6IjE2ODg5ODczNTUzODU3OTQiLCJQYWdlTmFtZSI6IiIsIk1haWwiOiJwbUB2YW5nZW5nLmNvbSIsIkNyZWF0ZVRpbWUiOiIyMDIzLTEwLTMxIDExOjExOjA3IiwiaXNzIjoibWluaW1heCJ9.dlfFfSWnzaFas4-hLh0wU7_JEop9mV7J9D9gC6sJMiBqF119Dl7TXnPzK8hs8TN09_9ZVHF0VVW4zhFTmsbKeqkjhqt-WDp8ewZfZiZK3J-lpGccPEFT1o4eCkMHeB4ODyafgn6F4r3BQ5K7_oLSWInMG4OW50L-AswCUWmwHExKQMuAMhLb1r0KcZxuru779tOrG_hvTYN1DMEhmglZbb5yQPHa9Ru23EHqgX88otbLs0z9hD4z_f0JuGz9BRudnKqPaC2KwKWte7Dm24UQHJuv4SsZVootDXC9SFaSlkehFZqqQDSK6raUbBiE7_3TdvkNIfouCjLZ3QHc67HCbA"
    url = "https://api.minimax.chat/v1/text/chatcompletion_pro?GroupId=" + group_id
    
    payload = {
        "bot_setting": [
            {
                "bot_name": "塔罗占卜师",
                "content": "请站在心理咨询师的角度，从用户的输入中识别用户的情感意图，并用 json 的格式回复；\n例如\n===\n\"input\":\"我明天运势怎么样？\"\n\"output\":{\"attend\":\"渴望获得好运，对现状可能不满\"}\n===\n如果不是心理咨询范畴的，或与主题无关的内容，请回复 {\"attend\":\"no\"}，\n答案只能是 json 格式的意图或 “no”，绝对不可以是其他的。\n===\n输入如下："
            }
        ],
        "messages": [{"sender_type": "USER", "sender_name": "小明", "text": user_input}],
        "reply_constraints": {"sender_type": "BOT", "sender_name": "塔罗占卜师"},
        "model": "abab5.5-chat",
        "tokens_to_generate": 1034,
        "temperature": 0.01,
        "top_p": 0.95,
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key
    }
    
    response = requests.post(url, headers=headers, json=payload)
    response_json = response.json()
    
    print("get_emotional_intent: ",response_json)
    return response_json["choices"][0]["messages"][0]["text"]


def get_tarot_response(question):
    group_id = "1688987355385794"
    api_key = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJOYW1lIjoidGFyb3RfYWdlbnQiLCJTdWJqZWN0SUQiOiIxNjg4OTg3MzU1ODUwODM2IiwiUGhvbmUiOiJNVGd3TWpVMk1qQXhORGM9IiwiR3JvdXBJRCI6IjE2ODg5ODczNTUzODU3OTQiLCJQYWdlTmFtZSI6IiIsIk1haWwiOiJwbUB2YW5nZW5nLmNvbSIsIkNyZWF0ZVRpbWUiOiIyMDIzLTEwLTMxIDExOjExOjA3IiwiaXNzIjoibWluaW1heCJ9.dlfFfSWnzaFas4-hLh0wU7_JEop9mV7J9D9gC6sJMiBqF119Dl7TXnPzK8hs8TN09_9ZVHF0VVW4zhFTmsbKeqkjhqt-WDp8ewZfZiZK3J-lpGccPEFT1o4eCkMHeB4ODyafgn6F4r3BQ5K7_oLSWInMG4OW50L-AswCUWmwHExKQMuAMhLb1r0KcZxuru779tOrG_hvTYN1DMEhmglZbb5yQPHa9Ru23EHqgX88otbLs0z9hD4z_f0JuGz9BRudnKqPaC2KwKWte7Dm24UQHJuv4SsZVootDXC9SFaSlkehFZqqQDSK6raUbBiE7_3TdvkNIfouCjLZ3QHc67HCbA"
    url = "https://api.minimax.chat/v1/text/chatcompletion_pro?GroupId=" + group_id
    
    payload = {
        "bot_setting": [
            {
                "bot_name": "塔罗占卜师",
                "content": "你是一个直播间的主播，现在直播的内容是塔罗占卜，但用户问了一个不属于塔罗可以解答的问题，请你根据他的问题，给出一段回答，目标是告诉用户，你只能回答塔罗相关的问题。\n\n\n在回答过程中，适当加入语气助词，增加一些人情味，答案尽量简短，高效。"
            }
        ],
        "messages": [{"sender_type": "USER", "sender_name": "小明", "text": question}],
        "reply_constraints": {"sender_type": "BOT", "sender_name": "塔罗占卜师"},
        "model": "abab5.5-chat",
        "tokens_to_generate": 1034,
        "temperature": 0.01,
        "top_p": 0.95,
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key
    }
    
    response = requests.post(url, headers=headers, json=payload)
    response_json = response.json()

    print("get_tarot_response: ",response_json["choices"][0]["messages"][0]["text"])
    
    return response_json["choices"][0]["messages"][0]["text"]

def get_final_answer(user_name,user_question):
    response = is_tarot_question(user_name,user_question)
    is_question = parse_answer(response)
    
    if is_question == '1':
        #输出引导词
        # 神女祭司已接收到____(用户id）的虔诚信念
        user_guide="神女祭司已接收到"+user_name+"的虔诚信念。"
        wav_data_PATH=request_and_save_wav(user_guide, "zh")

        async_play_wav_windows(wav_data_PATH)

        start_time = time.time()

        # 输出固定guide音频 
        AUDIO_DIR = 'wav\\guide_wav'
        TRACKING_FILE = 'utils\\selected_audios.txt'
        wav_data_PATH=get_random_audio(AUDIO_DIR,TRACKING_FILE)
        async_play_wav_windows(wav_data_PATH)

        # answer,cards = tarot_answer(content)
        # final_answer = transform_text(answer)
        filename = 'utils\\danmu.txt'

        cards = draw_random_cards_with_orientation('./utils/tarot_cards.json', num_cards=3)
        intend = get_emotional_intent(user_question)
        answer = tarot_answer(user_question, intend, cards)
        final_answer = transform_text(str(answer))

        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Code executed in {execution_time:.2f} seconds")

        text = user_name + "，您抽到的牌是：" + cards


        # 使用'with'语句确保文件正确关闭，并指定使用'utf-8'编码
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(text + '\n')  # '\n' 添加一个新行符


        start_time = time.time()
        # time.sleep(5)
        
        user_question=user_name,"关于你提到的"+user_question+"这个问题，下面我们进行抽卡占卜，请在心中默念你的问题。"
        wav_data_PATH=request_and_save_wav(user_question, "zh")

        async_play_wav_windows(wav_data_PATH)

        print("正在执行音频转换请求")
        wav_data_PATH = request_and_save_wav(final_answer, "zh")
        async_play_wav_windows(wav_data_PATH)

        # 更新前显的弹幕
        # 文件名
        # filename = 'utils\\danmu.txt'

        # 要写入的文本
        text = user_name + "，您抽到的牌是：" + cards

        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Code executed in {execution_time:.2f} seconds")
        time.sleep(5)

        print(final_answer)
        return final_answer
    else:
        answer = get_tarot_response(user_question)
        final_answer = transform_text(str(answer))
        wav_data_PATH = request_and_save_wav(final_answer, "zh")
        async_play_wav_windows(wav_data_PATH)
        return final_answer

# @app.route('/get_answer', methods=['POST'])
def get_answer(user_name,user_question):
    # data = request.json
    # user_question = data.get('user_question')
    
    # if not user_question:
    #     return jsonify({"error": "user_question is required"}), 400

    final_answer = get_final_answer(user_name,user_question)
    # print(final_answer)


    return final_answer

if __name__ == '__main__':
    get_answer("小明崽","我明天运气怎么样")
#     app.run(port=4090)
