import sys  # 导入 sys 模块，用于访问标准输入 sys.stdin

line_count = 0  # 初始化计数器，用于统计输入的行数

# 遍历标准输入中的每一行（例如从终端键入、或通过管道/重定向传入）
# sys.stdin是一个“标准输入流对象”，类似一个“文件”
for line in sys.stdin:
    line_count += 1  # 每读取一行，就将计数器加一

# 所有输入处理完后，输出总行数
print(line_count, "lines")
