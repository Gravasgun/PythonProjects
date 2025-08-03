#!/usr/bin/env python3

import sys
import os

# 获取命令行参数，例如: "1:filename" 或 ":filename"
args = sys.argv
target_arg = args[1]  # 获取第一个参数

# 以冒号分隔为提交号与文件名
target_arg = target_arg.split(":")
number = target_arg[0]      # 提交编号，可能是空字符串（表示 index）
filename = target_arg[1]    # 要查看的文件名

# ========= 查看某次提交中的文件内容 =========
if len(number) != 0:
    # 构造提交目录路径，例如 ".mygit/commits/1"
    TARGET_DIR = f".mygit/commits/{number}"

    # 如果该提交目录不存在，输出错误信息并退出
    if not os.path.exists(TARGET_DIR):
        print(f"mygit-show: error: unknown commit '{number}'")
        sys.exit(1)

    # 如果目标文件存在于该提交目录中，读取并打印内容
    if os.path.exists(TARGET_DIR + "/" + filename):
        with open(TARGET_DIR + "/" + filename) as f:
            content = f.read()
            print(content, end="")  # 使用 end="" 防止多输出一个换行
    else:
        # 如果文件在提交目录中不存在，输出错误信息
        print(f"mygit-show: error: '{filename}' not found in commit {number}")

# ========= 查看暂存区（index）中的文件内容 =========
else:
    # 构造 index 中的文件路径
    if os.path.exists(".mygit/index/" + filename):
        with open(".mygit/index/" + filename) as f:
            content = f.read()
            print(content, end="")  # 保持文件原本格式输出
    else:
        # 如果文件在暂存区中不存在，输出错误信息
        print(f"mygit-show: error: '{filename}' not found in index")
