import sys
# 星号 * 是解包运算符，它把列表中的每个元素当作单独的参数传递给 print 函数
# print()函数默认用空格连接多个参数
print(*sys.argv[1:])