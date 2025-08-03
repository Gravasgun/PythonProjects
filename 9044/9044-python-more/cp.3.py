import sys  # 导入 sys 模块，用于处理命令行参数和退出程序

# 检查命令行参数个数是否为 3（程序名 + 输入文件名 + 输出文件名）
if len(sys.argv) != 3:
    print(f"Usage:{sys.argv[0]}  <infile> <outfile>")  # 提示正确用法
    sys.exit(1)  # 异常退出，状态码 1 表示错误

try:
    # 使用 with 自动管理文件打开和关闭，读取输入文件，写入输出文件
    with open(sys.argv[1], "r", encoding="utf-8") as infile:
        with open(sys.argv[2], "w", encoding="utf-8") as outfile:
            lines = infile.readlines()
            outfile.writelines(lines)
except OSError as e:
    # 捕获文件操作中出现的错误（如文件不存在、权限不足等）
    print(f"{sys.argv[0]},error: {e}", file=sys.stderr)  # 打印错误信息
    sys.exit(1)  # 异常退出，状态码 1
