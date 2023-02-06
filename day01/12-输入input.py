"""
input 主要是用于 输入用户信息
既然是用户输入信息，我们是要定义一个变量来接收用户输入的数据
语法：
变量名 = input("提示信息")

1.  input（） 是用户输入的信息，我们一般要定义一个变量来接收数据
    input() 里 进行书写一些提示信息
2. input 会一直等待你的输入。 输入 enter(回车) 输入结束
3. 变量名对应的数据 类型为 字符串类型
"""
# 接收用户输入的密码
password = input("请输入密码:")

# 打印
print(password)
# print('password')  不要加引号
# 查看变量的类型
print( type(password) )