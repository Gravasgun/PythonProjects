#!/usr/bin/env python3

import os
import sys
import re
import shutil
import filecmp

# 从命令行获取提交信息参数
args = sys.argv[1:]
have_option_a = False
# 判断是否有 "-a"选项
if len(args) == 2:
    message = args[1]
else:
    have_option_a = True
    message = args[2]

# 定义路径常量
MYGIT_DIR = ".mygit"
INDEX_DIR = os.path.join(MYGIT_DIR, "index")
TARGET_DIR = os.path.join(MYGIT_DIR, "commits")
STRUCTURE_MARK = os.path.join(INDEX_DIR, "structure_change.txt")  # 统一结构变更标记

# 如果".mygit/commits"目录不存在，则创建
if not os.path.exists(TARGET_DIR):
    os.mkdir(TARGET_DIR)

# 获取 index 中的所有文件
file_names = os.listdir(INDEX_DIR)
# 排除标记文件
if "structure_change.txt" in file_names:
    file_names.remove("structure_change.txt")

# 如果有 -a 选项，将当前目录下存在的文件重新复制到 index 中
if have_option_a:
    for file_name in file_names:
        if os.path.exists(file_name):
            shutil.copy2(file_name, os.path.join(INDEX_DIR, file_name))


# 辅助函数：获取当前最大提交号
def get_max_dir_num(dir: str):
    result_list = []
    file_names = os.listdir(dir)
    for file_name in file_names:
        if re.search("^[0-9]+$", file_name):
            result_list.append(int(file_name))
    return max(result_list)


# =========== 初次提交 ================
if os.listdir(TARGET_DIR) == []:
    os.mkdir(os.path.join(TARGET_DIR, "0"))

    # 将暂存区中的所有文件复制到"commits/0"中
    for file in file_names:
        shutil.copy2(os.path.join(INDEX_DIR, file), os.path.join(TARGET_DIR, "0", file))

    # 创建"messages"目录用于存放提交信息文件
    os.mkdir(os.path.join(TARGET_DIR, "messages"))

    # 写入提交信息到 "commit_0.txt" 文件，并移动到 messages 目录
    with open("commit_0.txt", "w") as commit_file:
        commit_file.write(message)
    shutil.move("commit_0.txt", os.path.join(TARGET_DIR, "messages", "commit_0.txt"))

    # 清除结构性变更标记
    if os.path.exists(STRUCTURE_MARK):
        os.remove(STRUCTURE_MARK)

    print(f"Committed as commit 0")

# =================== 后续提交（commit N） ===================

else:
    # 获取当前最新提交目录的编号
    max_dir_num = get_max_dir_num(TARGET_DIR)
    # 获取上一次提交的完整路径
    last_commit_dir = os.path.join(TARGET_DIR, str(max_dir_num))
    # 获取上一次提交目录路径下的所有文件
    last_version_file_names = os.listdir(os.path.join(TARGET_DIR, str(max_dir_num)))
    # 获取index目录下的所有文件
    latest_file_names = os.listdir(INDEX_DIR)

    # 排除标记文件
    if "structure_change.txt" in latest_file_names:
        latest_file_names.remove("structure_change.txt")

    # 判断是否有结构性变更记录（即是否有结构变化行为）
    has_structure_change = False
    if os.path.exists(STRUCTURE_MARK):
        with open(STRUCTURE_MARK) as f:
            lines = f.readlines()
            if any(line.strip() for line in lines):
                has_structure_change = True

    # 比较 index 与上次提交是否一致（文件集合 + 文件内容）
    is_equal = True
    if not has_structure_change:
        if set(last_version_file_names) != set(latest_file_names):
            is_equal = False
        else:
            for file in latest_file_names:
                if file in last_version_file_names:
                    a_path = os.path.join(last_commit_dir, file)
                    b_path = os.path.join(INDEX_DIR, file)
                    if not filecmp.cmp(a_path, b_path, shallow=False):
                        is_equal = False
                        break

    if is_equal and not has_structure_change:
        print("nothing to commit")
        sys.exit(1)

    # 创建新的提交目录
    new_commit_dir = os.path.join(TARGET_DIR, str(max_dir_num + 1))
    os.mkdir(new_commit_dir)

    # Step 1: 复制上一版本文件
    for file in last_version_file_names:
        src = os.path.join(last_commit_dir, file)
        dst = os.path.join(new_commit_dir, file)
        shutil.copy2(src, dst)

    # Step 2: 删除 index 中已不存在的文件（说明被 rm --cached）
    for file in last_version_file_names:
        if file not in latest_file_names:
            path_to_remove = os.path.join(new_commit_dir, file)
            if os.path.exists(path_to_remove):
                os.remove(path_to_remove)

    # Step 3: 用 index 中的文件覆盖（新增或修改）
    for file in latest_file_names:
        src = os.path.join(INDEX_DIR, file)
        dst = os.path.join(new_commit_dir, file)
        shutil.copy2(src, dst)

    # Step 4: 写入提交信息
    commit_txt_name = f"commit_{max_dir_num + 1}.txt"
    with open(commit_txt_name, "w") as commit_file:
        commit_file.write(message)
    shutil.move(commit_txt_name, os.path.join(TARGET_DIR, "messages", commit_txt_name))

    # 清除结构性变更标记（提交完成）
    if os.path.exists(STRUCTURE_MARK):
        os.remove(STRUCTURE_MARK)

    print(f"Committed as commit {max_dir_num + 1}")
