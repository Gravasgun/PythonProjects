import pandas as pd
import numpy as np

# 1.使用字典的方式创建DataFrame
dict = {
    "姓名": ["张三", "李四", "王五"],
    "年龄": [18, 19, 20],
    "性别": ["男", "女", "男"]
}
print(f"使用字典的方式创建DataFrame：{pd.DataFrame(dict)}")
"""
使用字典的方式创建DataFrame：
   姓名  年龄 性别
0  张三  18  男
1  李四  19  女
2  王五  20  男
注意事项：
    使用字典的方式创建DataFrame，字典的key会变成列名，而对应key的值会变成对应列的值
    使用index可以指定行名，如果不指定，默认为0开始的整数数组
"""

# 2.嵌套列表
arr = [['张三', 18, 80], ['李四', 19, 90], ['王五', 20, 100]]
print(f"使用嵌套列表创建DataFrame：{pd.DataFrame(arr, columns=["姓名", "年龄", "成绩"])}")
"""
使用嵌套列表创建DataFrame：
   姓名  年龄   成绩
0  张三  18   80
1  李四  19   90
2  王五  20  100
注意事项：
    嵌套列表的每一行对应表中的一行数据，而列名则通过columns参数来指定
"""

# 3.使用numpy数组
arr2 = np.array([['张三', 18, 80], ['李四', 19, 90], ['王五', 20, 100]])
df = pd.DataFrame(arr2, columns=["姓名", "年龄", "成绩"])
print(f"使用numpy数组创建DataFrame：{df}")
"""
使用numpy数组创建DataFrame：
   姓名  年龄   成绩
0  张三  18   80
1  李四  19   90
2  王五  20  100
注意事项：
    与使用嵌套列表相似，需要使用columns来指定列名
"""
