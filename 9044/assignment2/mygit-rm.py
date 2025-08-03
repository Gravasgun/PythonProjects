#!/usr/bin/env python3

import sys
import re
import os
import filecmp

# 获取所有命令行参数
args = sys.argv

# 标志变量
have_force = False
have_cached = False

# 文件名列表
file_names = []

# 目录常量
INDEX_DIR = ".mygit/index"
STRUCTURE_CHANGE_MARK = os.path.join(INDEX_DIR, "structure_change.txt")

# 判断是否传入 --force 和 --cached
for arg in args:
    if "--force" in arg:
        have_force = True
    if "--cached" in arg:
        have_cached = True

# 提取文件名参数
if not have_force and not have_cached:
    file_names = args[1:]
elif have_force and have_cached:
    file_names = args[3:]
else:
    file_names = args[2:]

# 执行四种模式之一
if not have_force and not have_cached:
    # 严格模式
    for file in file_names:
        index_file_path = os.path.join(INDEX_DIR, file)

        # 检查工作区和 index 是否存在该文件
        if not os.path.exists(file):
            print(f"mygit-rm: error: '{file}' not found in current directory", file=sys.stderr)
            sys.exit(1)
        if not os.path.exists(index_file_path):
            print(f"mygit-rm: error: '{file}' is not in the mygit repository", file=sys.stderr)
            sys.exit(1)

        # 判断内容是否一致
        files_are_equal = filecmp.cmp(file, index_file_path, shallow=False)

        # 判断是否为结构性变化
        in_structure_change = False
        if os.path.exists(STRUCTURE_CHANGE_MARK):
            with open(STRUCTURE_CHANGE_MARK) as f:
                changed_files = {line.strip() for line in f}
                if file in changed_files:
                    in_structure_change = True

        # 允许删除的条件：内容相同 且 无结构性变化
        if files_are_equal and not in_structure_change:
            os.remove(index_file_path)
            os.remove(file)

            # 记录结构性删除（可选）
            with open(STRUCTURE_CHANGE_MARK, "a") as f:
                f.write(f"{file}\n")

        else:
            print(f"mygit-rm: error: '{file}' has staged changes in the index", file=sys.stderr)
            sys.exit(1)

elif have_force and have_cached:
    # 强制仅删 index
    for file in file_names:
        index_file_path = os.path.join(INDEX_DIR, file)
        if not os.path.exists(index_file_path):
            print(f"mygit-rm: error: '{file}' is not in the mygit repository", file=sys.stderr)
            sys.exit(1)
        os.remove(index_file_path)

elif have_force and not have_cached:
    # 强制删 index 和工作区
    for file in file_names:
        index_file_path = os.path.join(INDEX_DIR, file)
        if not os.path.exists(file):
            print(f"mygit-rm: error: '{file}' not found in current directory", file=sys.stderr)
            sys.exit(1)
        if not os.path.exists(index_file_path):
            print(f"mygit-rm: error: '{file}' is not in the mygit repository", file=sys.stderr)
            sys.exit(1)
        os.remove(index_file_path)
        os.remove(file)

elif not have_force and have_cached:
    # 仅删 index
    for file in file_names:
        index_file_path = os.path.join(INDEX_DIR, file)
        if not os.path.exists(index_file_path):
            print(f"mygit-rm: error: '{file}' is not in the mygit repository", file=sys.stderr)
            sys.exit(1)
        os.remove(index_file_path)
