#!/usr/bin/env python3

import sys
import re

result_lines = []        # 保存包含最大值的所有行
overall_max = float('-inf')  # 初始最大值设为负无穷
numbers = list()         # 存放当前行提取到的所有数字

while True:
    line = sys.stdin.readline()
    if line == "":
        break  # 读取结束

    # 提取该行中所有数字（支持整数和小数）
    number_list = re.findall(r"[-+]?\d+(?:\.\d+)?", line)

    numbers.clear()  # 清空上一行的数字列表
    for number in number_list:
        if number.isdigit():
            numbers.append(int(number))     # 整数
        else:
            numbers.append(float(number))   # 小数

    if numbers:  # 如果该行确实包含数字
        current_max = max(numbers)
        if current_max > overall_max:
            overall_max = current_max
            result_lines = [line]           # 替换为新的最大行
        elif current_max == overall_max:
            result_lines.append(line)       # 追加同样的最大行

# 输出所有包含最大值的行，顺序不变
for line in result_lines:
    print(line, end="")
