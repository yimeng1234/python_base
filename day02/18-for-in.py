"""
for in  for循环语句

语法：
for 临时变量 in 容器：
    循环体代码1
    循环体代码2
    ...

1. for 是关键字 .for 后边要有空格
2. 临时变量 起什么名字都可以。它只是一个临时的变量
3. in 也是关键字
4. 容器  -- 我们暂时知道是就是 字符串。所以 先用字符串代替
5. 一定记得 for 最后 要添加 冒号
"""
# 定义一个字符串 name
name = 'it'
# temp 临时的
for temp in name:
    print(temp)
# 最后写一个没有缩进的print
print('over')