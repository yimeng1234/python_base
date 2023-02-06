# 定义2个变量
num1 = 100
num2 = 200
# 交换
# 1. 先运算等号 右边
# 2. 元组是不可以修改的
# (num2,num1)
# (200,100)
# num1,num2 = (200,100)
# num1 = 200
# num2 = 100

# num1,num2 = num2,num1
# 写法一样
num1,num2 = (num2,num1)

print(num1,num2)
