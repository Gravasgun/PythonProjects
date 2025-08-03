#!/usr/bin/env python3

import os
import sys

# 定义 mygit 仓库的根目录名称
MYGIT_DIR = ".mygit"

# 获取当前程序名（去除路径部分），用于后续错误提示中展示
# 例如执行脚本为 ./mygit-init，则 prog 为 "mygit-init"
prog = os.path.basename(sys.argv[0])

# ========== 错误处理：如果仓库已存在则报错 ==========

# 如果 .mygit 目录已存在，说明仓库已初始化，输出错误信息并退出
if os.path.exists(MYGIT_DIR):
    print(f"{prog}: error: {MYGIT_DIR} already exists", file=sys.stderr)
    sys.exit(1)  # 退出状态码 1 表示出错

# ========== 尝试初始化 mygit 仓库 ==========

try:
    # 创建 .mygit 仓库目录
    os.mkdir(MYGIT_DIR)

    # 初始化成功，打印提示信息到标准输出
    print(f"Initialized empty mygit repository in {MYGIT_DIR}")

except Exception as e:
    # 如果创建目录失败（如权限问题），打印错误信息并退出
    print(f"{prog}: error: failed to create {MYGIT_DIR}", file=sys.stderr)
    sys.exit(1)  # 退出状态码 1 表示出错
