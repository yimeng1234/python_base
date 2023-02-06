
# 列表数据    data_list_1 = [1,5,2,9]    data_list_1.sort()    [1,2,5,9]
data_list = [
    {"name":'tom',"age":20},        # item.get(age)          20
    {"name":'jack',"age":18},       # item.get(age)          18
    {"name":'rose',"age":66},       # item.get(age)          66
    {"name":"lili","age":30}        # item.get(age)          30
]
# 对这个数据进行排序 应该是 拿到 年龄
# data_list[0]  {"name":'tom',"age":20}
# print(data_list[2].get('age') )
# data_list.sort(key = 匿名函数)
# data_list.sort(key = lamdba 参数：表达式)
# 匿名函数的作用 就是获取到 字典数据的age
# 排序 类似于 遍历，应该拿到每一个元素
# lamdba 参数 : 表达式
# 匿名函数的参数  就是 相当于 遍历的每一个元素
# item = {"name":'tom',"age":20}
# lambda item ：  item.get('age')
data_list.sort( key= lambda item : item.get('age') )
# lambda 形参 ： 形参.get('xxx')
print(data_list)





# def 函数名(参数):
#   代码1 -- 用参数

# 匿名  函数
# lambda 参数: 表达式
# 1. 关键字 lambda
# 2. 参数不限制数量
# 3. 表达式就一个 而且表达式的值会返回。 虽然没有return
# get_2_sum = lambda num1,num2 : num1 + num2
# print( get_2_sum(1,1) )










