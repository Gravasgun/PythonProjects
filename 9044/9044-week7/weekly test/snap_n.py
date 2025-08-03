#!/usr/bin/env python3

import sys

times = int(sys.argv[1])  # 从命令行参数中获取数字 N，表示触发输出的重复次数

dict = dict()  # 创建一个空字典，用于记录每一行输入的出现次数

while True:
    input = sys.stdin.readline()  # 从标准输入读取一行（包含换行符）
    if input == "":
        break  # 如果读到空字符串，说明输入结束，跳出循环

    if input not in dict:
        dict[input] = 1  # 如果该行第一次出现，将其加入字典并设为1次
    else:
        dict[input] += 1  # 如果该行已出现过，则计数加1
        if dict[input] == times:
            print(f"Snap: {input}", end="")  # 第N次出现时输出，并结束程序
            break