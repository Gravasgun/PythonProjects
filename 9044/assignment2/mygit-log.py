#!/usr/bin/env python3

import os
import sys
import re

# 指向提交信息所在目录
TARGET_DIR = ".mygit/commits/messages"

# 尝试读取该目录下所有的提交信息文件
try:
    file_names = os.listdir(TARGET_DIR)
except Exception as e:
    # 如果目录不存在或出错，打印错误并退出程序
    print(e)
    sys.exit(1)


# 定义提取 commit 编号的函数，从文件名中提取出数字部分
# 例如 "commit_12.txt" → 12
def extract_commit_number(name):
    return int(name.split('_')[1].split('.')[0])

# 对文件名按照编号从大到小排序（最新提交在最前面）
sorted_commits = sorted(file_names, key=extract_commit_number, reverse=True)

# 遍历排序后的提交信息文件
for file_name in sorted_commits:
    # 去掉文件名中的 "commit_" 和 ".txt"，只保留数字编号
    commit_number = re.sub(r"commit_", "", file_name)
    commit_number = re.sub(r".txt", "", commit_number)

    # 打开该提交文件并读取其中内容
    with open(os.path.join(TARGET_DIR, file_name), "r") as f:
        commit_message = f.read()

    # 输出格式为：编号 + 空格 + 提交信息
    print(f"{commit_number} {commit_message}")