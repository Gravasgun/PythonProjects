import numpy as np

# 示例一：生成单个随机整数
num1 = np.random.randint(10)
print(num1)

# 示例二：生成随机整数，指定上限
num2 = np.random.randint(1, 20)
print(num2)

# 示例三：生成二维数组
arr1 = np.random.randint(1, 10, (3, 4))
print(arr1)

# 示例四：生成指定类型的二维数组
arr2 = np.random.randint(1, 10, (3, 4), dtype="int64")
print(arr2)

# 示例五：生成指定长度，指定范围的一位数组
arr3 = np.random.randint(1, 20, 5)
print(arr3)
