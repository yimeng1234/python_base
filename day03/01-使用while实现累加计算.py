"""
语法： while
1. 初始化计数器变量
2. 判断条件
3. 在循环体中修改计数器
i = 1
while i<=100:
    print("媳妇我错了")
    i = i + 1   # i += 1

# 从 0 ~ 100 进行累加计算
            result = 0
            result = result + i

0           0  =  0 + 0
1           1  = 0 + 1
2           3  = 1 + 2
3           6  = 3 + 3
4           10 = 6 + 4
5           15 = 10 + 5
6           21 = 15 + 6
...
100

"""

# 1. 通过while循环 先把0~100 设计出来
# 2. 再通过定义一个 result 变量 来累加 循环值
# 初始化计数器
i = 0
# 定义一个 变量 来记录结果
result = 0
# while 判断
while i <= 100:

    # 让它累加
    result = result + i  # result += i
    print(i)
    # 修改计数器
    i = i + 1           # i += 1

print(result)
