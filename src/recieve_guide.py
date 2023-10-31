import json
import time
from test1 import get_answer
from utils.get_random_audio import get_random_audio
from tarot_easy import get_final_answer, is_tarot_question, parse_answer, tarot_answer, transform_text


from voice_in import async_play_wav_windows, request_and_save_wav


import json


def load_config(filename="config.json"):
    with open(filename, 'r', encoding='utf-8') as file:
        config = json.load(file)
    return config

def extract_content(received_data):
    flag=False

    # 将 'Data' 键的值从字符串转换为字典
    data_dict = json.loads(received_data['Data'])
    # 从字典中提取Nickname和Content
    nickname = data_dict['User']['Nickname']
    content = data_dict['Content']
    
    #提取到用户名和提问
    print("Received:", nickname, content)

    # 更新前显的弹幕
    # 文件名
    filename = 'utils\\danmu.txt'

    # 要写入的文本
    text = nickname + "   " + content

    wav_data_PATH=request_and_save_wav(content, "zh")

    async_play_wav_windows(wav_data_PATH)

    # 使用'with'语句确保文件正确关闭，并指定使用'utf-8'编码
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text + '\n')  # '\n' 添加一个新行符


    
    config=load_config(filename="wav\\trigger\\triggers.json")
    for trigger in config['triggers']:
        if trigger['word'] in content:
            print(trigger['text'])
            flag=True
            async_play_wav_windows(trigger['audioUrl'])
            break  # 如果找到了触发词，就跳出循环

    if not flag:


        result=get_answer(nickname,content)


        # # 确定问题是否可以回答
        # response = is_tarot_question(content)
        # is_question = parse_answer(response)

        # time.sleep(2)

        # if is_question == "1":
        #     start_time = time.time()

        #     # 输出固定guide音频 
        #     wav_data_PATH=get_random_audio()
        #     async_play_wav_windows(wav_data_PATH)

        #     answer,cards = tarot_answer(content)
        #     final_answer = transform_text(answer)
        #     end_time = time.time()
        #     execution_time = end_time - start_time
        #     print(f"Code executed in {execution_time:.2f} seconds")


        #     # 使用'with'语句确保文件正确关闭，并指定使用'utf-8'编码
        #     with open(filename, 'a', encoding='utf-8') as file:
        #         file.write(text + '\n')  # '\n' 添加一个新行符


        #     start_time = time.time()
        #     # time.sleep(5)
            
        #     user_question="关于你提到的"+content+"这个问题，下面我们进行抽卡占卜，请在心中默念你的问题。"
        #     wav_data_PATH=request_and_save_wav(user_question, "zh")

        #     async_play_wav_windows(wav_data_PATH)

        #     print("正在执行音频转换请求")
        #     wav_data_PATH = request_and_save_wav(final_answer, "zh")
        #     async_play_wav_windows(wav_data_PATH)

        #     # 更新前显的弹幕
        #     # 文件名
        #     # filename = 'utils\\danmu.txt'

        #     # 要写入的文本
        #     text = nickname + "，您抽到的牌是：" + cards

        #     end_time = time.time()
        #     execution_time = end_time - start_time
        #     print(f"Code executed in {execution_time:.2f} seconds")
        #     time.sleep(5)
            
        # # elif is_question == "0":
        #     # print('NO')
        #     # 输出不能回答
        #     # print("问题无法回答")
        #     # async_play_wav_windows("refuse_answer_wav\0c2b3322-7545-11ee-80e9-0242ac110005.wav")

        # else:
        #     print("问题无法回答")
        #     async_play_wav_windows("refuse_answer_wav\\0c2b3322-7545-11ee-80e9-0242ac110005.wav")

        #     print('error')

        






    return content
