import pandas as pd

# 1.列表(默认索引)
arr = [1, 2, 3, 4, 5]
series_example1 = pd.Series(arr, name='num')
print(f"列表(默认索引):{series_example1}")
"""
列表(默认索引):
0    1
1    2
2    3
3    4
4    5
Name: num, dtype: int64
注意事项：
    第一列是索引，因为并未在参数列表中指定索引index,所以默认是数字0开始；
    第二列是元素值，是传入的arr列表的元素的值；
"""

# 2.列表(指定索引)
arr2 = [1, 2, 3, 4, 5]
series_example2 = pd.Series(arr2, index=['a', 'b', 'c', 'd', 'e'])
print(f"列表(指定索引):{series_example2}")
"""
列表(指定索引):
a    1
b    2
c    3
d    4
e    5
dtype: int64
注意事项：
    使用了index指定索引，所以默认索引会被覆盖
"""

# 3.字典
dict = {"姓名": "张三", "年龄": 18, "性别": "男"}
series_example3 = pd.Series(dict, name="学生信息")
print(f"使用字典的方式创建Series:{series_example3}")
"""
使用字典的方式创建Series:
姓名    张三
年龄    18
性别     男
Name: 学生信息, dtype: object
注意事项：
    使用字典的方式创建Series，字典中的key会变成索引，字典中的值会变成值
"""

# 4.标量
series_example4 = pd.Series(5, name="使用标量创建Series")
print(f"使用标量的方式创建series：{series_example4}")
"""
使用标量的方式创建series：0    5
Name: 使用标量创建Series, dtype: int64
注意事项：
    使用标量创建 Series 时，元素的个数等于你传入的索引个数
"""