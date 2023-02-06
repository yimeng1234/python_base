
#定义一个字典
dict_data = {
    'name': "itheima",
    "age": 20,
    "address":"北京"
}

# 字典的 修改和 新增
# 语法： 字典变量名[key（键）] = 值

# 新增
dict_data['like'] = 'girl'
print(dict_data)
# 修改
dict_data['name'] = '如花'
print(dict_data)

# 在字典数据中根据给出的键删除对应值
# 字典.pop(key)
dict_data.pop('address')
print(dict_data)

#######字典的查询###############################
# 方式1
# 语法： 字典变量名.get(key)
n = dict_data.get('name')
print(n)

# 方式2
# 变量名 = 字典变量名[key]
name = dict_data['name']
print( name )
######字典的遍历  keys################################
# 字典变量名.keys()  获取这个字典的所有key值
for temp in dict_data.keys():
    print(temp)
    # 获取value值
    #dict_data.get(temp)

######字典的遍历 values################################
# 打印 50遍 字符串
print("*"*50)

# 字典变量名.values() 获取这个字典的所有value值
# item 每一项
for value in dict_data.values():
    print(value)
#####字典的遍历  items 获取 键和值#################################
# 字典变量名.items()
# 获取字典的 key和value
print("#"*50)
# ('name', '如花')
# for item in dict_data.items():

"""
dict_data = {
    'name': "itheima",          item
    "age": 20,                  item
    "address":"北京"            item
}
"""
# for (key,value) in dict_data.items():
for key,value in dict_data.items():
    print(f'key:{key},value:{value}')
    # print(item)
    #pass
    # 循环体的内容 我暂时还不想写，但是 不写语法不对
    # 可以 使用 pass 占位