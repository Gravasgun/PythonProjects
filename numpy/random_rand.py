import numpy as np

# 示例 1：生成一个 1D 数组
arr1 = np.random.rand(5) # 如果只传入一个整数，生成的是一个一维数组；如果传入多个整数，则生成相应维度的数组
print(arr1)

# 示例 2：生成一个 2D 数组
arr2 = np.random.rand(3,4)
print(arr2)

# 示例 2：生成一个 3D 数组
arr3 = np.random.rand(2,3,4)
print(arr3)