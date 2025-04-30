import pandas as pd

# 创建一个 DataFrame
data = {
    "姓名": ["张伟", "李娜", "王强"],
    "性别": ["男", "女", "男"],
    "年龄": [18, 17, 18],
    "数学": [85, 78, 90],
    "英语": [92, 88, 81]
}
df = pd.DataFrame(data)

# 保存为 CSV 文件
df.to_csv('/Users/liuhangji/Desktop/Pandas数据集/students_info2.csv', index=False, encoding='utf-8-sig')
print("CSV 文件已保存")
