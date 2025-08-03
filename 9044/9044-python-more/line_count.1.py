import sys

lines=sys.stdin.readlines()
# 使用 sys.stdin.readlines() 一次性读取所有输入行，返回一个字符串列表，每行作为一个元素
# print(lines) 输出：['1\n', '2\n', '3\n']
line_count = len(lines)
print(line_count,"lines")