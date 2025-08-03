#!/usr/bin/env python3

import os
import sys
import shutil
import re

# 定义常量
MYGIT_DIR = ".mygit"
COMMITS_DIR = os.path.join(MYGIT_DIR, "commits")
INDEX_DIR = os.path.join(MYGIT_DIR, "index")
RESTORE_MARK = os.path.join(INDEX_DIR, ".restored_from_commit")

program_name = os.path.basename(sys.argv[0])

# 检查 mygit 仓库存在
if not os.path.exists(MYGIT_DIR):
    print(f"{program_name}: error: mygit repository directory {MYGIT_DIR} not found", file=sys.stderr)
    sys.exit(1)

# 创建 index 目录（如果不存在）
if not os.path.exists(INDEX_DIR):
    os.mkdir(INDEX_DIR)

# 提取参数（添加的文件列表）
files = sys.argv[1:]


# 获取最近一次提交目录
def get_latest_commit_dir():
    if not os.path.exists(COMMITS_DIR):
        return None
    commit_ids = [name for name in os.listdir(COMMITS_DIR) if re.fullmatch(r"\d+", name)]
    if not commit_ids:
        return None
    commit_ids = sorted([int(i) for i in commit_ids])
    return os.path.join(COMMITS_DIR, str(commit_ids[-1]))


latest_commit_dir = get_latest_commit_dir()
restored_files = []

# 逐个处理要添加的文件
for file in files:
    # 情况 1：当前目录存在该文件 → 直接复制到 index/
    if os.path.exists(file):
        shutil.copy2(file, os.path.join(INDEX_DIR, file))
    # 情况 2：当前目录不存在，但上一版本存在 → 从 commits/ 中复制进 index/
    elif latest_commit_dir and os.path.exists(os.path.join(latest_commit_dir, file)):
        shutil.copy2(os.path.join(latest_commit_dir, file), os.path.join(INDEX_DIR, file))
        restored_files.append(file)
    # 情况 3：两个地方都没有，报错
    else:
        print(f"{program_name}: error: can not open '{file}'", file=sys.stderr)
        sys.exit(1)

# 记录恢复的文件名列表（供 commit 脚本识别）
if restored_files:
    with open(RESTORE_MARK, "a") as f:
        for f_name in restored_files:
            f.write(f"{f_name}\n")
