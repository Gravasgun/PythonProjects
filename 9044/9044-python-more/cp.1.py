import sys  # 导入 sys 模块，用于处理命令行参数和退出程序

# 判断参数个数是否为 3（程序名 + 输入文件名 + 输出文件名）
if len(sys.argv) != 3:
    # 如果参数不足或过多，打印用法提示信息
    print(f"Usage:{sys.argv[0]}  <infile> <outfile>")
    sys.exit(1)  # 异常退出，状态码 1 表示错误

# 使用 with 语句打开输入文件，自动管理关闭操作
with open(sys.argv[1], "r", encoding="utf-8") as infile:
    # 使用嵌套的 with 语句打开输出文件
    with open(sys.argv[2], "w", encoding="utf-8") as outfile:
        # 逐行读取输入文件的内容
        for line in infile:
            # 直接写入输出文件（line 本身自带换行符 \n，无需额外添加
            outfile.write(line)
