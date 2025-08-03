#!/usr/bin/env python3
import sys
import re

dict = dict()         # 创建一个空字典，用于保存每种鲸鱼的统计数据（pods数量和鲸鱼总数）
file_list = list()    # 创建一个列表，用于存放命令行传入的文件名

# 遍历命令行参数（跳过脚本名），将每个文件名加入 file_list
for file in sys.argv[1:]:
    file_list.append(file)

# 遍历每个输入的文件
for file in file_list:
    with open(file) as infile:
        for line in infile:
            # 使用正则表达式将连续的空白字符（空格、tab等）压缩为一个空格
            str = re.sub("\s+", " ", line)
            # 按空格最多分成 3 段：日期、鲸鱼数量、物种名称（包含多个单词）
            result = re.split(" ", str, maxsplit=2)
            # 提取鲸鱼数量并转为整数类型（注意：此处假设数据格式是合法的）
            count = int(result[1])
            # 提取物种名称，去掉两边空白并统一为小写，便于归一化处理
            species = result[2].strip().lower()
            # 如果物种名以 "s" 结尾，删除尾部的 's'，题目允许这样处理为“单数形式”
            if species.endswith("s"):
                species = species[:-1]
            # 如果该物种不在字典中，说明第一次出现：初始化 pod 数为 1，总数为当前数量
            if species not in dict:
                dict[species] = [1, count]
            else:
                # 如果已经存在，则更新：pod 数 +1，鲸鱼总数累加
                value = dict[species]
                dict[species] = [value[0] + 1, value[1] + count]

# 遍历字典中的所有物种，按字母顺序输出结果
for key in sorted(dict.keys()):
    print(f"{key} observations: {dict[key][0]} pods, {dict[key][1]} individuals")