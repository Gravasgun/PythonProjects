#!/usr/bin/env python3
import sys
import re

file_list = list()
sum = 0

# 把命令行参数中传入的文件名依次加入 file_list 列表
for file in sys.argv[1:]:
    file_list.append(file)

# 遍历每一个文件
for filename in file_list:
    with open(filename) as file:
        # 遍历文件的每一行
        for line in file:
            # 使用正则表达式匹配包含 " Orca" 的行，并提取前面的数字
            # 正则表达式说明：
            #   - " +": 匹配一个或多个空格（用于跳过日期和数量之间的间隔）
            #   - "(\d+)": 捕获一组连续数字，即鲸鱼的数量；括号表示“分组”，稍后可以通过 group(1) 获取
            #   - " Orca": 匹配空格+单词Orca，表示这一行是Orca类鲸鱼
            result = re.search(r" +(\d+) Orca", line)

            # 一定要判断是否匹配成功，否则 result 是 None，调用 group(1) 会报错
            if result:
                # 提取捕获组中的数字，去除两边空格后转换为整数并累加
                sum += int(result.group(1).strip())

# 最终输出统计结果，格式符合题目要求
print(f"{sum} Orcas reported")
