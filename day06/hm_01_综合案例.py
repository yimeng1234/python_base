students = [
    {"name":"张三","age":20},
    {"name":"李四","age":20},
    {"name":"王五","age":20}
]

# 1. 接收用户输入的 用户名
# 2. 对列表数据 进行遍历。 遍历获取每一项。
# 3. 如果相等 则格式化输出
# 4. 如果不相等 则提示没有找到



# 输入一个用户的名字，然后进行查找。如果找到就按照格式进行输出
# 如果找不到 输出找不到
def select_student():
    # 1. 接收用户输入的 用户名
    name = input("输入要查找的人物名字:")
    # 定义一个标记位--布尔值。 True 表示找到了， False 没有找到
    ok = False
    # 2. 对列表数据 进行遍历。 遍历获取每一项。
    for item in students:
        #item = {"name":"王五","age":20}
        #   根据每一项的 name进行比对
        if item.get('name') == name:
            # 3. 如果相等 则格式化输出
            print(f"查找的姓名为{item.get('name')} 年龄为{item.get('age')}")
            # 找到之后，就停止查找
            ok = True
            break
    # for循环结束之后，如果找到了 ok 肯定是True
    # for循环结束之后，没有找到  ok 还是 False
    if ok == False:             # if not ok:   if not False
        # 4. 如果不相等 则提示没有找到
        print(f"{name}没有找到")
# 调用
select_student()