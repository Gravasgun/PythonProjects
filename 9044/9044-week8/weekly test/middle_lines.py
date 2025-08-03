#!/usr/bin/env python3

import sys  # 用于读取命令行参数和退出程序
import re   # （虽然导入了，但这个脚本中没用到）

# 从命令行参数中获取文件名
file = sys.argv[1]

line_counter = 0        # 用于记录总行数
line_number = 1         # 用于标记当前行号，从1开始
line_dict = dict()      # 用字典存储每一行内容，键为行号，值为该行文本

# 打开并读取文件内容
with open(file) as f:
    for line in f:
        line_counter += 1                  # 累加总行数
        line_dict[line_number] = line      # 将当前行存入字典
        line_number += 1                   # 行号加一

    # 如果文件为空，直接退出
    if line_counter == 0:
        sys.exit(0)

    else:
        # 情况一：总行数为奇数，例如 5 → 输出第 3 行
        if line_counter % 2 != 0:
            target_line_number = int((line_counter / 2) + 1)
            print(line_dict[target_line_number], end="")

        # 情况二：总行数为偶数，例如 6 → 输出第 3 和第 4 行
        else:
            target_line_number = int(line_counter / 2)
            print(line_dict[target_line_number], end="")
            print(line_dict[target_line_number + 1], end="")
