import sys

# 模拟echo "#@"，打印所有传入的参数，使用range实现
# 从 sys.argv[1] 开始遍历每一个命令行参数（跳过程序名）
for i in range(1, len(sys.argv)):
    if i > 1:
        print(" ", end="")         # 从第二个参数开始，前面加空格分隔
    print(sys.argv[i], end="")     # 打印当前参数，末尾不换行

print()  # 所有参数输出完毕后换行
