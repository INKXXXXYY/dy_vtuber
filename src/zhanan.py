import requests



def send_post_request(url, params):
    """
    发送POST请求并返回响应对象。

    :param url: 请求的URL。
    :param params: 请求的参数，格式为字典。
    :return: requests.Response对象。
    """
    try:
        response = requests.post(url, data=params)
        response.raise_for_status()  # 确保请求成功
        return response
    except requests.RequestException as e:
        print(f"请求错误: {e}")
        return None

def send_get_request(url, params=None):
    """
    发送GET请求并返回响应对象。

    :param url: 请求的URL。
    :param params: 请求的参数，格式为字典。
    :return: requests.Response对象。
    """
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # 确保请求成功
        return response
    except requests.RequestException as e:
        print(f"请求错误: {e}")
        return None

# 初始化全局变量
global initial_response
initial_response = None

# 在程序启动时执行第一个GET请求
url1 = "http://170.106.67.116:8848/thread/create"
params1 = {"assistant_id": "asst_OMC8Pv5vqhZ0AiFMdzuJgIxT"}
initial_response = send_get_request(url1, params1)


def process_request_flow(content):
    """
    使用全局变量initial_response的结果来处理第二个请求，并打印响应内容。
    """
    global initial_response

    # 假设您需要从响应中提取 'thread_id'
    if initial_response:
        response_data = initial_response.json()  # 将响应转换为字典
        thread_id = response_data.get('thread_id')  # 从字典中安全地提取 'thread_id'

        # 第二个请求的信息
        url2 = "http://170.106.67.116:8848/run"
        params2 = {
            "assistant_id": "asst_k5hCz7MH4wI4ksBkOpt8IiyX",
            "thread_id": thread_id,
            "message": content
        }

        # 发送第二个请求
        response2 = send_post_request(url2, params2)

        if response2:
            # 提取并打印第二个请求的响应内容
            response_data = response2.json()
            print(response_data['response'])
        else:
            print("第二个请求失败")
    else:
        print("第一个请求失败或未执行")

    return response_data['response']
