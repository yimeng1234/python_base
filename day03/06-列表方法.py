
#####count ##########################
# 列表.count(要统计的元素)
# 统计被测试值出现的次数
data_list_1 = [ 'python','java','php','c','python' ]
num = data_list_1.count('p')
print(num)
#######append##########################
# 列表.append(数据)
# 在列表的末尾添加数据
# 将 字符串 添加到 列表中，成为 最后一个元素
data_list_1.append('c++')
print(data_list_1)

data_list_1.append([1,2,3])
print(data_list_1)
########pop#########################
# 列表.pop()
# 删除指定索引对应的数据
# pop() 默认删除最后一个元素
# pop(index)  index 索引。可以指定删除某一个
print(data_list_1)
temp = data_list_1.pop()
print(temp)
# print(data_list_1)
# data_list_1.pop(2)
# print(data_list_1)
#######修改列表数据 -- 列表[索引] = 新数据##########################
print(data_list_1)
# 列表[索引] = 新数据
data_list_1[4] = '666'
print(data_list_1)
########reverse  反转#########################
# a 现在属于 变量名
# data_list_3 = [a,b,c,d,e]   单独这么写不对，因为 a没有定义
# 列表.reverse()
# 反转列表, 将列表中的元素倒序
data_list_2 = [1,2,3,4,5]

data_list_2.reverse()
print(data_list_2)

#########sort 排序########################
# sort 就是排序
# sort() 默认是 升序 也就是说 sort(reverse=False)
# 如果想要降序 就是 sort(reverse=True)
data_list_3 = [1,5,2,4,3]

# 列表.sort()
data_list_3.sort(reverse=True)
print(data_list_3)

#########sort 排序 扩展 ########################
data_list_4 = ['1','3','2','tom','jack']
data_list_4.sort()
# 0 48
# A 65
# a 97
print(data_list_4)