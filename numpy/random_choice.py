import numpy as np
import numpy.random

#  示例 1: 从 1, 2, 3, 4, 5 中随机选取 3 个元素，允许重复
arr1 = np.random.choice([1, 2, 3, 4, 5], size=3, replace=True)
print(arr1)

# 示例 2: 从 1, 2, 3, 4, 5 中随机选取 3 个元素，不允许重复
arr2 = np.random.choice([1, 2, 3, 4, 5], size=3, replace=False)
print(arr2)

# 示例 3: 使用概率分布来选择元素，选择的概率不均匀
arr3 = np.random.choice([1, 2, 3, 4, 5], size=3, replace=True, p=[0.1, 0.2, 0.1, 0.2, 0.4])
print(arr3)

# 示例 4: 生成一个包含多个维度的数组
arr4 = np.random.choice([1, 2, 3, 4, 5], size=(2, 3), replace=True)
print(arr4)

# 示例 5: 生成一个从 0 到 9 的数组，并选择其中的 3 个元素
arr5 = numpy.random.choice(10, size=3, replace=False)
print(arr5)
