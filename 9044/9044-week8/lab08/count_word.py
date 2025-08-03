#!/usr/bin/env python3

import sys
import re

# 从标准输入（stdin）一次性读取所有行，返回一个字符串列表，每个元素是一行
lines = sys.stdin.readlines()

# 创建一个空字典，用于统计每个英文单词出现的次数
word_dict = dict()

# 从命令行参数中获取要查找的目标单词
# 例如运行时命令：./count_word.py death < lyrics.txt，则 target = "death"
target = sys.argv[1]

# 遍历每一行文本
for line in lines:
    # 去除前后空白后，如果该行是空行，跳过
    if len(line.strip()) == 0:
        continue
    else:
        # 将所有非英文字母的字符（标点符号、数字等）替换为空格
        result = re.sub(r"[^a-zA-Z]", " ", line)

        # 将多个连续空格替换为一个空格（标准化空白字符）
        result = re.sub(r"\s+", " ", result)

        # 使用正则表达式提取所有由英文字母组成的单词列表
        word_list = re.findall(r"[a-zA-Z]+", result)

        # 遍历每个单词，转为小写后统计出现次数
        for word in word_list:
            word_lower = word.lower()  # 转小写，确保大小写不敏感
            if word_lower not in word_dict:
                word_dict[word_lower] = 1  # 第一次出现，设为 1
            else:
                word_dict[word_lower] += 1  # 后续出现，计数加一

# 使用字典的 get 方法获取目标单词出现次数（如果不存在则返回 0）
# 同样转为小写确保匹配时大小写不敏感
print(f"{target} occurred {word_dict.get(target.lower(), 0)} times")
