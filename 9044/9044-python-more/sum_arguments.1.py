import sys  # 导入 sys 模块，用于获取命令行参数和标准错误输出

total = 0  # 初始化一个累加变量，用于计算所有整数参数的总和

for arg in sys.argv[1:]:  # 遍历所有命令行参数（跳过程序名本身）
    try:
        total += int(arg)  # 尝试将当前参数转换为整数并累加到 total 中
    except ValueError:
        # 如果转换失败，说明参数不是合法整数，输出错误信息到标准错误输出
        # file参数代表重定向
        print(f"error: '{arg}' is not an integer", file=sys.stderr)
        sys.exit(1)  # 程序异常退出，状态码为 1 表示错误

# 如果所有参数都成功转换为整数，打印总和
print("Sum of the number is ", total)
