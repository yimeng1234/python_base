"""
由于循环条件始终满足, 程序持续执行起来不会停止的现象, 称为死循环
"""
# while 永远为真:
#   执行 循环体的代码
# while True:
#     print("一直循环")

# 1. 初始化 计数器
i = 1

# 2. 判断计数器
while i <= 10:
    print("我会一直运行下去")

# i += 1 并没有在循环体 里边 不会随着循环而执行
# 是等到 循环结束后，才会执行
    i += 1

print('over')