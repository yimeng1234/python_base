"""
for 临时变量 in range(循环次数)：
    循环体
注意事项： 循环是从 0 开始的
"""
# for i in range(10):
#     print(i)

# 1. 使用for range 实现数据的循环 把 0~100 获取
# 2. 再累加
result = 0
for i in range(101):
    print(i)
    #累加
    result = result + i

print(result)

