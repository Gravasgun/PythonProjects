#!/usr/bin/env python3

import sys
import re
import os
import filecmp

# 获取所有命令行参数
args = sys.argv

# 初始化两个标志变量：是否包含 --force 和 --cached
have_force = False
have_cached = False

# 初始化要处理的文件名列表
file_names = []

# 定义 index 目录路径
INDEX_DIR = ".mygit/index"

# ========== 检查是否传入 "--force" 选项 ==========
for arg in args:
    is_force = re.search(r"--force", arg)
    if is_force is not None:
        have_force = True
        break

# ========== 检查是否传入 "--cached" 选项 ==========
for arg in args:
    is_cached = re.search(r"--cached", arg)
    if is_cached is not None:
        have_cached = True
        break

# ========== 根据选项组合提取需要处理的文件名 ==========
# 无参数时直接从 argv[1:] 取全部文件名
if have_force == False and have_cached == False:
    file_names = sys.argv[1:]
# 如果同时有 --force 和 --cached，文件名从 argv[3:] 开始
elif have_force == True and have_cached == True:
    file_names = sys.argv[3:]
# 否则说明只存在一个选项，从 argv[2:] 开始提取文件名
else:
    file_names = sys.argv[2:]

# ========== 执行不同模式下的 rm 操作逻辑 ==========

# ---- 情况 1：既没有 --force 也没有 --cached，执行最严格检查 ----
if have_force == False and have_cached == False:
    for file in file_names:
        index_file_path = os.path.join(INDEX_DIR, file)

        # 1. 检查文件是否存在于工作目录（当前目录）
        if not os.path.exists(file):
            print(f"mygit-rm: error: '{file}' not found in current directory", file=sys.stderr)
            sys.exit(1)

        # 2. 检查文件是否存在于 index 暂存区
        elif not os.path.exists(index_file_path):
            print(f"mygit-rm: error: '{file}' is not in the mygit repository", file=sys.stderr)
            sys.exit(1)

        else:
            # 3. 文件存在于工作区与 index，比较它们是否完全相同
            files_are_equal = filecmp.cmp(file, index_file_path, shallow=False)
            if files_are_equal:
                os.remove(index_file_path)
                os.remove(file)
            else:
                print(f"mygit-rm: error: '{file}' has staged changes in the index", file=sys.stderr)
                sys.exit(1)
            """
            # 判断是否是恢复文件（出现在 .recovered_files 中）
            is_restored = False
            recovered_list_path = os.path.join(INDEX_DIR, ".recovered_files")

            if os.path.exists(recovered_list_path):
                with open(recovered_list_path) as f:
                    restored_set = set(line.strip() for line in f)
                    is_restored = file in restored_set
            # 如果完全一致且不是恢复文件，才允许正常删除
            if files_are_equal and not is_restored:
                os.remove(index_file_path)
                os.remove(file)
            else:
                # 如果是恢复文件，即使内容相同也不能直接删除
                # 不一致则报错：index 中文件与工作区不同
                print(f"mygit-rm: error: '{file}' has staged changes in the index", file=sys.stderr)
                sys.exit(1)
            """

# ---- 情况 2：同时传入 --force 和 --cached，仅删除 index 中的文件 ----
elif have_force == True and have_cached == True:
    for file in file_names:
        index_file_path = os.path.join(INDEX_DIR, file)

        # 如果 index 中不存在该文件，报错
        if not os.path.exists(index_file_path):
            print(f"mygit-rm: error: '{file}' is not in the mygit repository", file=sys.stderr)
            sys.exit(1)
        else:
            # 强制删除 index 中的文件（忽略工作区是否存在或一致性）
            os.remove(index_file_path)

# ---- 情况 3：只传入 --force，忽略一致性强制删除工作区 + index 文件 ----
elif have_force == True and have_cached == False:
    for file in file_names:
        index_file_path = os.path.join(INDEX_DIR, file)

        # 如果工作区中不存在，报错
        if not os.path.exists(file):
            print(f"mygit-rm: error: '{file}' not found in current directory", file=sys.stderr)
            sys.exit(1)

        # 如果 index 中不存在，也报错
        elif not os.path.exists(index_file_path):
            print(f"mygit-rm: error: '{file}' is not in the mygit repository", file=sys.stderr)
            sys.exit(1)

        else:
            # 同时删除 index 和工作区中的该文件
            os.remove(index_file_path)
            os.remove(file)

# ---- 情况 4：只传入 --cached，仅删除 index 中的文件（不管工作区） ----
elif have_force == False and have_cached == True:
    for file in file_names:
        index_file_path = os.path.join(INDEX_DIR, file)

        # 如果 index 中不存在，报错
        if not os.path.exists(index_file_path):
            print(f"mygit-rm: error: '{file}' is not in the mygit repository", file=sys.stderr)
            sys.exit(1)
        else:
            # 仅删除 index 中的文件
            os.remove(index_file_path)
