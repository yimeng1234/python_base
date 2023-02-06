"""
字符串.find(被查找字符)

被查找字符是否存在于当前字符串中, 如果存在则返加开始下标, 不存在则返回 -1
"""
name = 'itcast'
# name.find() 是返回查找到的索引
# 所以 需要用一个变量名 来接收数据值
# find 查找
result = name.find('e')
print(result)


##############replace 替换#########################################
"""
字符串.replace(原字符串, 新子字符串)
"""
str1 = '我在黑马程序员学习黑马'
new_str = str1.replace('黑马','白马')
print(new_str)
print(str1)

#########splite 按照字符来分割字符串####################
"""
字符串.split(分割符)
"""
str2 = 'keyword=神仙水&enc=utf-8&wq=神仙水'
# 字符串 根据 字符 进行分割，返回 分割的列表
# 变量名 = 字符串.split(分割符)
new_data = str2.split('&')
print(new_data)

#########join###############
"""
字符串.join(一般为列表)
把列表中的数据，通过一定的字符 连接 起来
"""
# 先 记住这个列表
data_list = [ 'python','java','html' ]
# 变量名 = '连接符'.join(列表)
new_str = '&'.join(data_list)
print(new_str)
