#!/usr/bin/env python3

import sys
import re
import glob
import math

# 存储每位艺人的词频模型：{艺人名: {"word_dict": 词频字典, "total_count": 总词数}}
artist_models = {}

# 构建整个语料的词汇集合（用于统计 vocab_size）
vocab_set = set()

# 遍历歌词目录中每个艺人的歌词文件
for path in glob.glob("lyrics/*.txt"):
    word_dict = {}        # 当前艺人的词频统计
    total_count = 0       # 当前艺人的总词数

    # 打开并读取歌词文件
    with open(path) as f:
        for line in f:
            # 替换所有非字母字符为空格（去标点、数字等）
            line = re.sub(r"[^a-zA-Z]", " ", line)

            # 提取所有英文单词
            words = re.findall(r"[a-zA-Z]+", line)

            # 累加当前行的单词数量
            total_count += len(words)

            # 将每个单词转小写并统计频次
            for word in words:
                word = word.lower()
                vocab_set.add(word)  # 加入到全局词汇表中
                word_dict[word] = word_dict.get(word, 0) + 1

    # 提取艺人名（去掉路径和扩展名）
    artist_name = re.sub(r"^lyrics/", "", path)
    artist_name = re.sub(r"\.txt$", "", artist_name)
    artist_name = artist_name.replace("_", " ")  # 下划线替换为空格

    # 保存该艺人的模型（词频字典 + 总词数）
    artist_models[artist_name] = {
        "word_dict": word_dict,
        "total_count": total_count
    }

# 统计总词汇表大小（用于理解语料范围，但这题中分母不使用它）
vocab_size = len(vocab_set)

# 遍历所有测试文件（每个文件是一段歌词，判断可能是哪个艺人写的）
for test_path in sys.argv[1:]:
    test_words = []

    # 读取并清洗测试文件中的歌词
    with open(test_path) as f:
        for line in f:
            line = re.sub(r"[^a-zA-Z]", " ", line)
            words = re.findall(r"[a-zA-Z]+", line)
            test_words.extend(word.lower() for word in words)  # 转小写

    best_artist = None              # 当前最有可能的艺人
    best_log_prob = float('-inf')  # 最佳 log 概率（初始为负无穷）

    # 对每位艺人计算该歌词段落的 log-probability
    for artist, model in artist_models.items():
        word_dict = model["word_dict"]
        total_count = model["total_count"]

        log_prob = 0  # 初始化对数概率为 0
        for word in test_words:
            count = word_dict.get(word, 0)  # 获取该词的出现次数（没有则为 0）
            prob = (count + 1) / total_count  # 应用加法平滑（只分子加 1）
            log_prob += math.log(prob)  # 累加 log 概率

        # 更新当前最高概率的艺人
        if log_prob > best_log_prob:
            best_log_prob = log_prob
            best_artist = artist

    # 输出匹配结果，格式严格匹配题目要求
    print(f"{test_path} most resembles the work of {best_artist} (log-probability={best_log_prob:.1f})")
