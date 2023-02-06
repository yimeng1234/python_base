
"""
with 语句 能够帮助我们 在操作完成之后，自动关闭文件操作
语法：
with open() as f:
    文件操作代码1
    文件操作代码2

1. with 是关键字 后边要有空格
2. open() 该怎么写就怎么写  encoding必须要使用 关键字参数
3. open() 会打开文件 我们使用 as 变量名 来接收 打开的变量
    变量名 起什么都可以 一般我们使用 f   file
4. with 最后要添加 冒号
5. with 里边的代码 要有缩进
"""
try:
    with open('data.txt', 'r', encoding='utf-8') as f:
        print("文件操作代码1")
        print("文件操作代码2")
except:
    print('文件不存在')
# 最后的这个print 和文件操作没有关系。因为它没有在with语句内
print('abc')