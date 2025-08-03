import sys  # 导入 sys 模块，用于获取命令行参数 sys.argv

total = 0   # 初始化一个变量 total，用来累加所有参数的整数值

# 遍历命令行传入的每一个参数（从 sys.argv[1] 开始，不包括程序名 sys.argv[0]）
for arg in sys.argv[1:]:
    total += int(arg)  # 将参数转换为整数后加到 total 中

# 输出累加结果，前面是提示信息，后面是结果值
print("Sum of the number is ", total)
