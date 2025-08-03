# 创建一个空字典，用于记录出现过的输入行
line_count = {}

# 无限循环读取用户输入
while True:
    try:
        # 从标准输入读取一行
        line = input("Enter line: ")
    except EOFError:
        # 如果用户按下 Ctrl+D（或 Ctrl+Z），触发 EOF，跳出循环
        break

    # 如果输入是空行，也退出循环
    if line == "":
        break

    # 如果这一行之前已经出现过
    if line in line_count:
        print("Snap!")  # 输出提示
    else:
        # 如果这一行是第一次出现，就记录下来
        line_count[line] = 1