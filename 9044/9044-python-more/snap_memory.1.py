line_seen = set()  # 初始化一个空集合，用于记录出现过的输入行

while True:
    try:
        line = input("Enter a line: ")  # 提示用户输入一行文本
    except EOFError:
        break  # 如果输入结束（如 Ctrl+D / Ctrl+Z），退出循环

    if line == "":
        break  # 如果用户输入的是空行，也退出循环

    if line in line_seen:
        print("Snap!")  # 如果该行已经出现过，打印提示信息
    else:
        line_seen.add(line)  # 如果是第一次输入该行，就加入集合
