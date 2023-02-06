"""
需求：
1. 提示用户输入两个数字
2. 使用获取到的数据进行加法运算
3. 在控制台输出计算结果，格式要求：xx + xx = xx
"""

# 1. 提示用户输入两个数字
num1 = input("请输入第一个数字：")
num2 = input("赶紧的输入第二个数字:")
# 2. 使用获取到的数据进行加法运算
# +
# input() 得到的数据 默认是 字符串
# 在进行 加法运行的时候 要把字符串转换为整形
# int(x)
result = int(num1) + int(num2)
# 3. 在控制台输出计算结果，格式要求：xx + xx = xx
# 注意 第3个大括号的写法！！！
print(f'{num1} + {num2} = {result}')


















print('{}+{}={}'.format(num1,num2,result))
print(f"{num1} + {num2} = {result}")