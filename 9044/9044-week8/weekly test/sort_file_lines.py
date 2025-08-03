#!/usr/bin/env python3

import sys  # 导入 sys 模块，用于从命令行读取参数

# 从命令行参数中获取文件名
file = sys.argv[1]

# 初始化一个空列表，用于存储每一行内容（去除换行符）
line_list = []

# 打开并读取文件内容
with open(file) as f:
    for line in f:
        line_list.append(line.strip())  # 去除每行末尾的换行符，并加入列表中

# 定义一个排序函数：返回一个元组，包含“行的长度”和“行本身”
# 排序规则：先按长度升序，如果长度相同再按字典序排序
def sort_key(line):
    return (len(line), line)

# 使用 sorted() 对行列表排序，key 参数指定排序依据为 sort_key 函数
sorted_line_list = sorted(line_list, key=sort_key)

# 输出排序后的每一行
for line in sorted_line_list:
    print(line)
