'''
int(x) 将x转换为一个整数 x是字符串时，必须是整数类型的字符串
float(x) 将x转换为一个浮点数 x是字符串时，只要是数字类型的字符串即可
str(x) 将 x 转换为字符串 对于任意数据类型x都可以转为字符串类型
'''

# 不能把非数值的字符串 转换为 整形
num = 'gogogo'

print( type( int(num) ) )

print("over")