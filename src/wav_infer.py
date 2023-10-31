import subprocess
import os

def run_inference_command(checkpoint_path, face_path, audio_path, working_directory):
    # 确保音频文件的绝对路径
    audio_path = os.path.abspath(audio_path)

    # 设置工作目录，确保包含 inference.py 文件的目录
    os.chdir(working_directory)

    # 构建命令
    command = [
        'python',
        'inference.py',
        '--checkpoint_path',
        os.path.abspath(checkpoint_path),  # 确保检查点文件的绝对路径
        '--face',
        os.path.abspath(face_path),  # 确保人脸视频文件的绝对路径
        '--audio',
        audio_path
    ]

    # 执行命令
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    # 检查命令是否成功执行
    if result.returncode == 0:
        print("命令执行成功！")
        print("输出信息:")
        print(result.stdout.decode('utf-8'))
    else:
        print("命令执行失败！")
        print("错误信息:")
        print(result.stderr.decode('utf-8'))

