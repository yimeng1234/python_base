# """
# 需求：按照以下要求完成代码的编写
#
# 第一步：录入学生信息
#     1)提示用户在控制台输入3个学生的信息，学生信息包含姓名、年龄
#     2)要求：封装录入单个学生信息的函数，并返回学生的信息
# 第二步：展示学生列表信息
#     1)封装打印学生信息的函数，格式要求如右图：
# 第三步：统计学生总数
#     1)封装获取学生总数的函数，并对该函数进行调用和数据打印
# 第四步：查询学生信息
#     1)封装根据学生姓名查询学生信息的函数
#     2)提示用户“请输入要查询的学生姓名：”
#     3)如果存在，直接在控制台打印学生信息，格式为：“姓名：张三，年龄：25”
#     4)如果不存在，直接在控制台打印“对不起，名字叫【张三】的学生不存在”
# """
#
# students = []
# def student01():
#     i = 0
#     while i<= 2:
#         name = input("请输入3个学生信息：姓名为：")
#         age = input("请输入3个学生信息：年龄为：")
#         students.append({
#             'name':name,
#             'age':age,
#             "id":i +1
#         })
#         i +=1
#     return students
# stu = student01()
# print(stu)
#
#
# # aaa = input("请输入要查询的学生姓名")
# for i in students:

#    print(f'{i.get(id),i.get(name),i.get(age)}')

# def showNumber(numbers):
#     for n in numbers:
#         print(n)
# showNumber(2.34)
# if 3 > 2:
#     print("数字3是大于2的")
# elif True:
#     print("这个条件是满足的")
# elif 5 <= 2:
#     print("5是小于等于2的")
# else:
#     print("上述条件都不满足")
# 7
# 以下Pyhton代码的运行结果是:
#
# i = 0
# j = 0
# while i < 3:
#     print('hello')
#     while j < 3:
#         print('hello')
#         break
#         j += 1
#     continue
#     i += 1




