#!/usr/bin/env python3

import sys    # 导入 sys 模块，用于访问命令行参数
import re     # 导入 re 模块，用于正则表达式匹配

# 初始化一个空列表，用于存放符合条件的字符串
result_list = list()

# 遍历所有从命令行输入的参数（第一个参数是脚本名，跳过）
for arg in sys.argv[1:]:
    # 使用正则表达式查找是否存在三个连续的元音字母（忽略大小写）
    match = re.search(r"[aeiouAEIOU]{3}", arg)

    # 如果找到了匹配项
    if match is not None:
        # 并且匹配的内容非空（这步其实多余，因为 {3} 保证非空）
        if len(match.group()) != 0:
            # 将该参数加入结果列表
            result_list.append(arg)

# 将所有匹配的参数用空格连接成字符串，并输出
print(" ".join(result_list))
