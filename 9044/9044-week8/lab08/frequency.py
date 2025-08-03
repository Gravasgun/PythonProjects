#!/usr/bin/env python3

import re
import sys
import glob     # 导入 glob 模块，用于匹配多个文件路径（支持通配符）

# 从命令行参数中获取要查找的目标单词，例如：python3 frequency.py love
target = sys.argv[1]

# 初始化一个空字典，用于统计单词频率
word_dict = dict()

# 初始化计数器，用于记录当前处理文本的总单词数量
counter = 0

# 使用 glob 匹配 "lyrics" 目录下所有以 .txt 结尾的文件，按文件名排序后逐个处理
for path in sorted(glob.glob("lyrics/*.txt")):

    # 每处理一个文件前，清空上一个文件的统计结果
    word_dict.clear()
    counter = 0

    # 以默认编码打开每个歌词文件
    with open(path) as file:
        # 按行读取文件内容
        for line in file.readlines():
            # 如果该行为纯空白或仅包含空格，则跳过
            if len(line.strip()) == 0:
                continue
            else:
                # 替换掉该行中所有非英文字母字符，改为空格（去标点、数字等）
                result = re.sub(r"[^a-zA-Z]", " ", line)

                # 将多个连续空格合并成一个空格（清洗多余空白）
                result = re.sub(r"\s+", " ", result)

                # 用正则表达式提取所有英文单词（连续字母组成）
                word_list = re.findall("[a-zA-Z]+", result)

                # 将当前行中的单词数量累加进总计数器
                counter += len(word_list)

                # 遍历每个单词，统计其出现次数（不区分大小写）
                for word in word_list:
                    word_lower = word.lower()
                    if word_lower not in word_dict:
                        word_dict[word_lower] = 1  # 首次出现，记为 1 次
                    else:
                        word_dict[word_lower] += 1  # 已出现，计数加 1

    # 从文件路径中提取出艺人名（去除前缀 "lyrics/" 和后缀 ".txt"）
    temppath = re.sub(r"lyrics/", "", path)
    artist = re.sub(r".txt", "", temppath)

    # 将艺人名中的下划线 "_" 替换为空格，更美观
    ture_artist = re.sub(r"_", " ", artist.strip())

    # 安全地获取目标单词出现次数（不存在则返回 0），计算其词频
    frequency = float(word_dict.get(target.lower(), 0)) / float(counter)

    # 按指定格式输出：出现次数 / 总单词数 = 频率（保留9位小数） 艺人名
    print(f"{word_dict.get(target.lower(), 0):4}/{counter:6} = {frequency:.9f} {ture_artist}")
