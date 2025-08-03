#!/usr/bin/env python3

import sys

# 用于去重判断的集合（set 的查找效率很高）
arg_set = set()

# 用于按顺序保存第一次出现的参数
result = list()

# 遍历命令行参数（跳过 sys.argv[0]，即脚本名）
for arg in sys.argv[1:]:
    # 如果该参数之前没出现过（即不在集合中）
    if arg not in arg_set:
        arg_set.add(arg)      # 加入集合用于去重
        result.append(arg)    # 加入结果列表，保留原始顺序

# 将结果列表中的所有参数用空格连接成一个字符串并输出
print(" ".join(result))