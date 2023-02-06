"""
需求：按照以下要求完成代码的编写

第一步：录入学生信息
    1)提示用户在控制台输入3个学生的信息，学生信息包含姓名、年龄
    2)要求：封装录入单个学生信息的函数，并返回学生的信息
第二步：展示学生列表信息
    1)封装打印学生信息的函数，格式要求如右图：
第三步：统计学生总数
    1)封装获取学生总数的函数，并对该函数进行调用和数据打印
第四步：查询学生信息
    1)封装根据学生姓名查询学生信息的函数
    2)提示用户“请输入要查询的学生姓名：”
    3)如果存在，直接在控制台打印学生信息，格式为：“姓名：张三，年龄：25”
    4)如果不存在，直接在控制台打印“对不起，名字叫【张三】的学生不存在”
"""
# 容器： 字符串，列表，元组，字典
# students 是全局变量 用于保存【记录】学生信息
# students = [
#     {"name":"张三","age":20},
#     {"name":"李四","age":20},
#     {"name":"王五","age":20}
# ]

# 是全局变量 用于保存【记录】学生信息
students = []
# record 记录
def record_student_info():
    # 1.初始化计数器
    i = 0
    # 2.循环判断
    while i<=2:
        username = input("输入姓名:")
        age = input("输入年龄：")
        # 把接收到的数据 放入数组中
        students.append({
            "name":username,
            "age":age,
            "id":i+1
        })
        #3. 计数器 +1
        i = i + 1
    # 如果我们需要返回数据 就可以添加 return
    return students
#调用记录
stu = record_student_info()
print(stu)
# print(students)
#######第二步##################################################
# students = [
#     {"name":"张三","age":20},
#     {"name":"李四","age":20},
#     {"name":"王五","age":20}
# ]
def show_students_info():
    print('-----学生列表信息-----')
    # 对字典列表进行遍历
    for item in students:
        #item = {"name":"张三","age":20}
        # item.get() item[]
        print(f"{item.get('id')} \t\t {item['name'] } \t\t {item.get('age')}")

    print('-'*20)

show_students_info()

#######统计学生个数#########################
def get_student_count():
    count = len(students)
    return count

c = get_student_count()
print(c)




