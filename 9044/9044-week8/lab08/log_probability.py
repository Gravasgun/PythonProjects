#!/usr/bin/env python3

import re
import sys
import glob
import math

# 定义一个字典用于记录某位歌手中各个单词出现的次数
word_dict = dict()

# 存储当前句子中每个词的 log 概率（即每个词的 log(P(w))）
frequency_list = list()

# 当前文本总单词数
counter = 0

# 存储当前歌手歌词中整句话的总 log 概率
final_result = 0

# 遍历 lyrics 目录下的所有歌词文件（每个文件对应一位歌手）
for path in sorted(glob.glob("lyrics/*.txt")):
    # 每处理一个新歌手前清空旧数据
    word_dict.clear()
    counter = 0
    final_result = 0
    frequency_list.clear()

    # 打开歌词文件，按行读取
    with open(path) as file:
        for line in file.readlines():
            # 跳过空行
            if len(line.strip()) == 0:
                continue

            # 用空格替换所有非字母字符（去除标点、数字等）
            result = re.sub(r"[^a-zA-Z]", " ", line)
            # 合并多个连续空格成一个空格
            result = re.sub(r"\s+", " ", result)
            # 提取出所有单词
            word_list = re.findall("[a-zA-Z]+", result)
            # 累加当前行的单词数量到总词数中
            counter += len(word_list)
            # 将每个单词转换为小写并统计出现次数
            for word in word_list:
                word_lower = word.lower()
                if word_lower not in word_dict:
                    word_dict[word_lower] = 1
                else:
                    word_dict[word_lower] += 1

    # 从路径中提取艺人名称，并将下划线替换为空格
    temppath = re.sub(r"lyrics/", "", path)
    artist = re.sub(r".txt", "", temppath)
    ture_artist = re.sub(r"_", " ", artist.strip())

    # 对命令行中传入的所有单词进行处理（例如 python3 script.py truth is beauty）
    for arg in sys.argv[1:]:
        # 取出当前单词的出现次数，若不存在则为 0
        count = word_dict.get(arg.lower(), 0)
        # 使用 add-1 平滑（即分子加 1，分母保持为当前总词数）
        frequency = float((count + 1) / counter)
        # 计算对数概率并添加到列表中
        frequency_list.append(math.log(frequency))

    # 把所有单词的 log 概率累加起来，得到整个句子的 log 概率
    for log in frequency_list:
        final_result += log

    # 按格式输出：总 log 概率 + 艺人名称
    print(f"{final_result:10.5f} {ture_artist}")
