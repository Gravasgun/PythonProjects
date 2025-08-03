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
INDEX_DIR = os.path.join(MYGIT_DIR, "index")  # 暂存区目录
TARGET_DIR = os.path.join(MYGIT_DIR, "commits")  # 提交历史目录
RESTORE_MARK = os.path.join(INDEX_DIR, ".recovered_files")  # 标记恢复文件

# 如果".mygit/commits"目录不存在，则创建
if not os.path.exists(TARGET_DIR):
    os.mkdir(TARGET_DIR)

# 获取当前暂存区（index）中的所有文件名
file_names = os.listdir(INDEX_DIR)
# 排除标记文件
if ".recovered_files" in file_names:
    file_names.remove(".recovered_files")

# 如果有-a选项，需要更新index目录下的文件
if have_option_a:
    for file_name in file_names:
        if os.path.exists(file_name):
            shutil.copy2(file_name, INDEX_DIR + "/" + file_name)

# 辅助函数：从提交目录中提取最大编号（用于创建新提交目录）
def get_max_dir_num(dir: str):
    result_list = []
    file_names = os.listdir(dir)
    for file_name in file_names:
        # 只提取纯数字的目录名（过滤掉messages目录）
        if re.search("^[0-9]+$", file_name):
            file_name = int(file_name)
            result_list.append(file_name)
    # 返回最大的编号值
    return max(result_list)

# =================== 初次提交（commit 0） ===================

# 如果提交目录为空，表示还没有任何提交，执行首次提交逻辑
if os.listdir(TARGET_DIR) == []:
    # 创建编号为"0"的提交目录
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

    # 清除恢复标记
    if os.path.exists(RESTORE_MARK):
        os.remove(RESTORE_MARK)

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
    if ".recovered_files" in latest_file_names:
        latest_file_names.remove(".recovered_files")

    # 判断是否存在恢复的文件
    has_recovered = False
    if os.path.exists(RESTORE_MARK):
        with open(RESTORE_MARK) as f:
            for line in f:
                restored_file = line.strip()
                if restored_file in latest_file_names:
                    has_recovered = True
                    break

    # 检查暂存区文件是否与上一次提交的文件内容完全相同
    is_equal = True
    # 判断"index目录下的文件的数量和内容"是否与"上一次提交的多个文件 一模一样"
    if not has_recovered:
        if set(last_version_file_names) != set(latest_file_names):
            is_equal = False
        else:
            for file in latest_file_names:
                if file in last_version_file_names:
                    abs_a_path = TARGET_DIR + "/" + str(max_dir_num) + "/" + file
                    abs_b_path = INDEX_DIR + "/" + file
                    if not filecmp.cmp(abs_a_path, abs_b_path, shallow=False):
                        is_equal = False
                        break

    # 如果文件内容完全一致且没有被恢复的文件，输出提示并终止提交
    if is_equal and not has_recovered:
        print("nothing to commit")
        sys.exit(1)

    # 创建新的提交目录，编号为 max_dir_num + 1
    new_commit_dir = os.path.join(TARGET_DIR, str(max_dir_num + 1))
    os.mkdir(new_commit_dir)

    # 没有改动的文件要复制到最新版的文件中去，相当于快照
    # Step 1: 复制上一版本的所有文件
    for file in last_version_file_names:
        src = os.path.join(last_commit_dir, file)
        dst = os.path.join(new_commit_dir, file)
        shutil.copy2(src, dst)

    # Step 2: 删除 index 中已不存在的文件（被 rm --cached 的文件）
    for file in last_version_file_names:
        if file not in latest_file_names:
            path_to_remove = os.path.join(new_commit_dir, file)
            if os.path.exists(path_to_remove):
                os.remove(path_to_remove)

    # Step 3: 用index 中的文件覆盖commits中的文件（新增/更新）
    for file in latest_file_names:
        src = os.path.join(INDEX_DIR, file)
        dst = os.path.join(new_commit_dir, file)
        shutil.copy2(src, dst)

    # 创建新的提交信息文件
    commit_txt_name = f"commit_{max_dir_num + 1}.txt"
    with open(commit_txt_name, "w") as commit_file:
        commit_file.write(message)

    # 移动提交信息文件到 messages 目录
    shutil.move(commit_txt_name, os.path.join(TARGET_DIR, "messages", commit_txt_name))

    # 清除恢复标记
    if os.path.exists(RESTORE_MARK):
        os.remove(RESTORE_MARK)

    print(f"Committed as commit {max_dir_num + 1}")
