import time
from tarot_easy import is_tarot_question, parse_answer, tarot_answer, transform_text
from voice_in import async_play_wav_windows, request_and_save_wav


def process_tarot_question(content):

    # 开始计时
    start_time = time.time()

    # 
    print("正在执行openai请求") 

    response = is_tarot_question(content)
    is_question = parse_answer(response)

    if is_question == "1":
        answer = tarot_answer(content)
        final_answer = transform_text(answer)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Code executed in {execution_time:.2f} seconds")

        start_time = time.time()
        time.sleep(5)
        print("正在执行音频转换请求")
        wav_data_PATH = request_and_save_wav(final_answer, "zh")
        async_play_wav_windows(wav_data_PATH)

        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Code executed in {execution_time:.2f} seconds")
        time.sleep(5)

    elif is_question == "0":
        print('NO')
    else:
        print('error')