#!/usr/bin/env python3
import sys
import re

# 从标准输入中一次性读取所有内容（例如通过重定向 < 输入）
content = sys.stdin.read()

# 初始化单词计数器
counter = 0

# 将文本按行拆分（不保留换行符），逐行处理
for line in content.splitlines():
    # 去除当前行两侧的空白字符后，判断是否是空行（完全为空或只有空格、制表符）
    if len(line.strip()) == 0:
        continue  # 空行跳过，不做处理
    else:
        # 使用正则表达式将当前行中所有非英文字母的字符替换为空格
        # 这样可以去掉标点符号、数字等，仅保留字母组成的单词
        result = re.sub("[^a-zA-Z]", " ", line)

        # 将多个连续的空格合并为一个空格，并去掉行首尾的空格
        result = re.sub(r"\s+", " ", result).strip()

        # 使用正则表达式查找所有由英文字母组成的单词
        # [a-zA-Z]+ 表示匹配一个或多个连续的英文字母
        word_list = re.findall(r"[a-zA-Z]+", result)

        # 将当前行中的单词数加入总计数器
        counter += len(word_list)

# 输出所有非空行中的英文单词总数
print(f"{counter} words")
