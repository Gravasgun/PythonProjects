import sys  # 导入 sys 模块，用于访问命令行参数列表 sys.argv

# 判断是否有命令行参数（排除程序名本身），即 sys.argv[1:] 是不是非空列表
if sys.argv[1:]:
    # 如果至少有一个参数，先打印第一个参数，且不换行
    # 例如：如果是 python script.py hello world，那么 sys.argv[1] 是 "hello"
    print(sys.argv[1], end='')

# 遍历第二个参数及其后的所有参数（如果有）
for arg in sys.argv[2:]:
    # 每个参数前加一个空格再输出，保持多个参数之间有空格间隔
    # 例如输出 " hello world"（注意前面加了空格）
    print('', arg, end='')

# 打印一个换行符，结束输出
print()