"""
break: 当某条件满足时, 退出当前循环语句

演示 吃苹果

吃5个苹果

while 三部曲

1. 初始化数据
2. 条件判断
3. 修改计数器
"""
# 1. 初始化数据
a = 1
# 2. 条件判断
while a <= 5:
    # 吃第 n 个 苹果
    print(f"吃第{a}个苹果")

    # if 别顶格 因为我们当前是在 循环体里
    # == 是进行条件判断
    if a == 3:
        # 停止循环
        break

    # 3. 修改计数器
    a = a + 1
    # a += 1

# print 没有缩进 和 while 循环 无关
print('over')