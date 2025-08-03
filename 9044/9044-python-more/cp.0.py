import sys  # 导入 sys 模块，用于处理命令行参数和退出程序

# 判断参数个数是否为 3（程序名 + 输入文件名 + 输出文件名）
if len(sys.argv) != 3:
    # 如果参数不足或过多，打印用法提示信息
    print(f"Usage:{sys.argv[0]}  <infile> <outfile>")
    sys.exit(1)  # 异常退出，状态码 1 表示错误

# 打开输入文件，模式为只读（"r"），使用 UTF-8 编码
infile = open(sys.argv[1], "r", encoding="utf-8")

# 打开输出文件，模式为写入（"w"），若文件已存在则清空，编码为 UTF-8
outfile = open(sys.argv[2], "w", encoding="utf-8")

# 遍历输入文件的每一行
for line in infile:
    # 将读取的每一行写入输出文件
    # file=outfile 表示写入到 outfile 文件
    # end="" 表示不要额外添加换行符（因为 line 本身自带 \n）
    print(line, file=outfile, end="")

# 关闭输入文件，释放资源
infile.close()

# 关闭输出文件，确保写入完成
outfile.close()
