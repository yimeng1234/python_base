"""
字典
语法： {
    key1: value,
    key2: value,
    key3: value
}
key: 一般都是字符串  这个字符串一般具有一定的含义
value: 数据值

注意： key是不能重复的
"""
# 方式1
dict_1 = {
    "name":"张三",
    "age":20,
    "no":18,
    "gender":"boy"
}
print( dict_1 )
print( type(dict_1) )

# 方式2
# 面向对象的定义方式
dict_2 = dict()
# 相当于
dict_3 = {}