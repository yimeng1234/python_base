"""
我们今天只需要记住 5个数据类型就可以
其他的 后续会学习
名称      例子          type打印结果

字符串     ‘it’            str
整数       5               int
浮点数     3.1             float
布尔值     False/True      bool
None        None            NoneType
列表      []              list
字典      {}              dict
元组      ()              tuple

我们想要打印 变量名 对应的数据值的类型，该怎么做呢？？
使用 type(变量名/数据值)
type 一般要结合 print配合使用

"""
# 姓名  -- 字符串
# 变量名 = 数据值
name = "itheima"
print(name)
# type(name)
# type 和print配合使用
print( type(name) )
# print( type('name') )
# 年龄  -- 整数
age = 15
print( type(age) )
# print( type('age') )
# 价格 -- 小数
price = 3.5
print( type(price) )
# 是否是人类 -- 布尔值  True/False
is_person = True
print( type(is_person) )
# 有女朋友了吗  -- NoneType
# 可以理解为 我声明了一个变量，还没有给变量 赋值
firend = None
print(  type(firend) )
