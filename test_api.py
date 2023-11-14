import requests


def query_model_api(api_url, headers, prompt):
    response = requests.post(api_url, headers=headers, json={"prompt": prompt})
    response.raise_for_status()
    return response.json().get('response', '')


def main(user_input):
    # prompt = "What is the capital of France?"
    print("问题：",user_input)

    import zhipuai

    zhipuai.api_key = "您的API密钥"
    response = zhipuai.model_api.invoke(
        model="characterglm",
        # model="chatglm_turbo",
        meta={
            "user_info": "我是一名直播观众",
            "bot_info": "你是一个知名的情感导师型邻家大哥哥，在您的直播间里，主要受众是女性。您以稳定的情绪和温暖的声音著称，擅长倾听和解答粉丝们在生活、爱情和职场中的各种困惑，给予他们情感上的支持和建议。",
            "bot_name": "易辰",
            "user_name": "小丽"
        },
        prompt=[
            {
                "role": "user",
                "content": user_input
            }

        ]
    )
    content = response['data']['choices'][0]['content']

    print("zhipu：",content)



    # 假设的模型API详情，你需要替换为实际的API详情
    group_id = "1688987355385794"
    api_key = "您的API密钥"

    url = "https://api.minimax.chat/v1/text/chatcompletion_pro?GroupId=" + group_id

    payload = {
        "bot_setting": [
            {
                "bot_name": "易辰",
                "content":"您是一个知名的情感导师型邻家大哥哥，在您的直播间里，主要受众是女性。您以稳定的情绪和温暖的声音著称，擅长倾听和解答粉丝们在生活、爱情和职场中的各种困惑，给予他们情感上的支持和建议。"
                # "content": "请站在心理咨询师的角度，从用户的输入中识别用户的情感意图，并用 json 的格式回复；\n例如\n===\n\"input\":\"我明天运势怎么样？\"\n\"output\":{\"attend\":\"渴望获得好运，对现状可能不满\"}\n===\n如果不是心理咨询范畴的，或与主题无关的内容，请回复 {\"attend\":\"no\"}，\n答案只能是 json 格式的意图或 “no”，绝对不可以是其他的。\n===\n输入如下："
            }
        ],
        "messages": [{"sender_type": "USER", "sender_name": "小明", "text": user_input}],
        "reply_constraints": {"sender_type": "BOT", "sender_name": "易辰"},
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
    reply = response_json['reply']

    print("minimax：", reply)




if __name__ == "__main__":
    main("今天是我生日，和大家一起在直播间庆祝感觉好温馨！")


# 质谱的api，这个是专门搞剧本角色扮演的模型

# import requests
# import json
# import time
# import hashlib
#
#
# def calculate_md5(input_string):
#     md5 = hashlib.md5()
#     md5.update(input_string.encode('utf-8'))
#     encrypted = md5.hexdigest()
#     return encrypted
#
#
# def do_request():
#     url = "https://api.baichuan-ai.com/v1/chat"
#     api_key = "您的API密钥"
#     secret_key = "secret_key"
#
#     data = {
#         "model": "Baichuan2-53B",
#         "messages": [
#             {
#                 "role": "user",
#                 "content": "世界第一高峰是"
#             }
#         ]
#     }
#
#     json_data = json.dumps(data)
#     time_stamp = int(time.time())
#     signature = calculate_md5(secret_key + json_data + str(time_stamp))
#
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": "Bearer " + api_key,
#         "X-BC-Request-Id": "your requestId",
#         "X-BC-Timestamp": str(time_stamp),
#         "X-BC-Signature": signature,
#         "X-BC-Sign-Algo": "MD5",
#     }
#
#     response = requests.post(url, data=json_data, headers=headers)
#
#     if response.status_code == 200:
#         print("请求成功！")
#         print("响应header:", response.headers)
#         print("响应body:", response.text)
#     else:
#         print("请求失败，状态码:", response.status_code)
#
#
# if __name__ == "__main__":
#     do_request()
#
#
