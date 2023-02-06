"""
不可变： 内存中的数据不允许被修改
    int,float,bool,str,tuple
可变： 内存中的数据允许被修改
    dict,list
"""
# 不可变类型
a = 1
print( id(a) )

a = 2
print( id(a) )

print('*'*50)

str1 = '没有情人的情人节'
print(str1)
print(id(str1))
print('#'*50)
# 字符串 + 拼接
str1 = str1 + "我感觉很孤独，你陪我吧"
print(str1)
print(id(str1))

#######可变类型########################################
print('$$'*20)
data_list = [1]
print( id(data_list) )
# 新增数据
data_list.append(2)
print(data_list)
print(id(data_list))

print("!"*30)
# 字典
data_dict = {
    "name":"itheima",
    "age":20,
    "sister": ["杨幂秘","林志玲玲","岳云鹏"]
}
print(id(data_dict))
# 新增
data_dict["address"]="bj"
data_dict.pop('sister')   #删除
print(data_dict)
print(id(data_dict))