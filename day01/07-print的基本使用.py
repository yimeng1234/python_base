"""
print(数据值/变量名)

print 可以一起打印很多的变量
print(变量名1，变量名2，...)
print(变量名，数据值，数据值，变量名，变量名,....)
"""
name = 'itheima'
age = 20
address = 'bj'

print(name)
print(age)

# 错误写法
# print('address')
# 可以 print('bj')
print(address)
# 可以打印很多的变量
print(name,age,address)

# 格式化数据
# 我的名字是 xxx ,我今年 xxx 岁，我住在 xxx
print('我的名字是',name,'，我今年',age,'岁，','我住在',address)