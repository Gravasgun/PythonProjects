import pandas as pd
import gymnasium as gym
import networkx as nx


# 创建 DataFrame
data = {
    "姓名": ["张伟", "李娜", "王强", "赵敏", "刘洋", "陈晨", "杨杰", "林静", "何明", "周婷"],
    "性别": ["男", "女", "男", "女", "男", "女", "男", "女", "男", "女"],
    "年龄": [18, 17, 18, 19, 17, 18, 17, 18, 19, 17],
    "数学": [85, 78, 90, 72, 88, 91, 84, 79, 86, 90],
    "英语": [92, 88, 81, 95, 86, 89, 82, 93, 77, 91]
}

data = pd.Series([1,2,3,4,5])
# 1.head()和tail()
print(data.head(2))
"""
0    1
1    2
dtype: int64
"""
print(data.head(4))
"""
   姓名 性别  年龄  数学  英语
0  张伟  男  18  85  92
1  李娜  女  17  78  88
2  王强  男  18  90  81
3  赵敏  女  19  72  95
"""
print(data.tail(2))
"""
3    4
4    5
dtype: int64
"""
print(data.tail(4))
"""
   姓名 性别  年龄  数学  英语
6  杨杰  男  17  84  82
7  林静  女  18  79  93
8  何明  男  19  86  77
9  周婷  女  17  90  91
"""

# shape
print(data.shape) # (5,)
print(data.shape) # (10, 5)

# columns
print(data.columns) # Index(['姓名', '性别', '年龄', '数学', '英语'], dtype='object')

# dtypes
print(data.dtypes) # int64
print(data.dtypes)
"""
姓名    object
性别    object
年龄     int64
数学     int64
英语     int64
dtype: object
"""

# info()
print(data.info())
"""
<class 'pandas.core.series.Series'>
RangeIndex: 5 entries, 0 to 4
Series name: None
Non-Null Count  Dtype
--------------  -----
5 non-null      int64
dtypes: int64(1)
memory usage: 172.0 bytes
None
"""
print(data.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 5 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   姓名      10 non-null     object
 1   性别      10 non-null     object
 2   年龄      10 non-null     int64 
 3   数学      10 non-null     int64 
 4   英语      10 non-null     int64 
dtypes: int64(3), object(2)
memory usage: 532.0+ bytes
None
"""

# describe()
print(data.describe())
"""
count    5.000000
mean     3.000000
std      1.581139
min      1.000000
25%      2.000000
50%      3.000000
75%      4.000000
max      5.000000
dtype: float64
"""
print(data.describe())
"""
              年龄         数学         英语
count  10.000000  10.000000  10.000000
mean   17.800000  84.300000  87.400000
std     0.788811   6.201254   5.834762
min    17.000000  72.000000  77.000000
25%    17.000000  80.250000  83.000000
50%    18.000000  85.500000  88.500000
75%    18.000000  89.500000  91.750000
max    19.000000  91.000000  95.000000
"""