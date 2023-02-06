"""
格式化输出
将程序的运行结果按照一定的格式输出
"""
name = '张三'
age = 20
address = '北京中南海旁边的小桥下'
# 我的名字是 xxx ,我今年 xxx 岁，我住在 xxx
# 字符串 可以使用 + 进行拼接
# age 是 整数
# 整形不能直接参与 字符串的拼接  -- 要把整数转换为字符串
# str(变量名/数据值)
print("我的名字是"+name+"我今年"+str(age)+"岁"+"我住在"+address)
print("我的名字是"+name+"我今年"+str(age)+"岁"+"我住在"+address)
print("我的名字是",name,"我今年",str(age),"岁","我住在:",address)