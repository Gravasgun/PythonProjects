#!/usr/bin/env python3

import os
import sys
import shutil
import re
import filecmp

# 定义常量
MYGIT_DIR = ".mygit"
COMMITS_DIR = os.path.join(MYGIT_DIR, "commits")
INDEX_DIR = os.path.join(MYGIT_DIR, "index")
STRUCTURE_CHANGE_MARK = os.path.join(INDEX_DIR, "structure_change.txt")  # 统一结构变更标记文件
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
structure_changed_files = []  # 用于记录结构性变更的文件名

# 逐个处理要添加的文件
for file in files:
    index_path = os.path.join(INDEX_DIR, file)

    # 情况 1：当前目录存在该文件
    if os.path.exists(file):
        # 如果 index 中已存在且内容一致 → 不处理
        if os.path.exists(index_path) and filecmp.cmp(file, index_path, shallow=False):
            continue  # 文件内容未变，跳过

        # 否则，复制文件到 index
        shutil.copy2(file, index_path)

        # 判断是否结构性变更：当前文件也存在于最近一次 commit 中
        if latest_commit_dir and os.path.exists(os.path.join(latest_commit_dir, file)):
            structure_changed_files.append(file)

    # 情况 2：工作区没文件，但最近一次提交中有 → 是恢复文件
    elif latest_commit_dir and os.path.exists(os.path.join(latest_commit_dir, file)):
        shutil.copy2(os.path.join(latest_commit_dir, file), index_path)
        structure_changed_files.append(file)

    # 情况 3：两个地方都找不到
    else:
        print(f"{program_name}: error: can not open '{file}'", file=sys.stderr)
        sys.exit(1)


# 统一结构性变更标记写入文件
if structure_changed_files:
    with open(STRUCTURE_CHANGE_MARK, "a") as f:
        for f_name in structure_changed_files:
            f.write(f"{f_name}\n")
