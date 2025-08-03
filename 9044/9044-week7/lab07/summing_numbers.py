#!/usr/bin/env python3
# 指定使用 python3 解释器来运行该脚本

import sys  # 导入 sys 模块，用于获取命令行参数
import re   # 导入 re 模块，用于使用正则表达式提取数字

sum = 0  # 用于累计所有文件中提取到的数字之和

# 遍历所有从命令行传入的文件名（跳过 sys.argv[0]，即脚本自身）
for file in sys.argv[1:]:
    with open(file) as infile:  # 打开每一个文件，使用 with 自动关闭文件
        for line in infile:  # 遍历文件的每一行
            # 使用正则表达式查找所有连续数字（\d+ 表示1位或多位数字）
            # 返回的是一个字符串列表，例如 ['12', '3']
            result = re.findall(r'\d+', line)

            # 如果该行中包含至少一个数字
            if len(result) != 0:
                # 遍历所有提取到的数字字符串
                for number in result:
                    # 将字符串转为整数并加到总和中
                    sum += int(number)

# 输出最后的总和
print(sum)