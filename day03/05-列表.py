"""
列表的定义
语法：
    [ 元素1,元素2,...  ]
    元素可以说  字符串，整数，浮点数，布尔值
"""
# 方式1  记住
list_1 = [ '张三', '李四','王五','赵六',True, 666 ]
print( type(list_1) )
print(list_1)
# 方式2  了解一下。 属于 面向对象的 方式
# 空列表
list_2 = list()
# 等价于
list_3 = []
print( type(list_2) )

# 通过 索引 下标的形式 来获取列表中的某一个数据
# 变量名 = 列表[索引]
# 索引不要超过 预期的长度
zhao = list_1[3]
print(zhao)





