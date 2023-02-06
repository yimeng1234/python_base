
# 1. mode 如果是读 可以不写。默认就是读  推荐大家 写上
with open('data.txt', 'r', encoding='utf-8') as f:
    # f.read()  是把文件的内容一次性 都读取
    content = f.read()
    print(content)

print('*'*20)
# 一行一行读取文件内容
with open('data.txt', 'r', encoding='utf-8') as file:
    # 一行一行读取适用于 大文件
    # line 行
    # readline() 一行一行读
    one = file.readline()
    print(one,end='')       # end='' 意思是 把打印的 换行 去掉 这里要用关键字参数
    two = file.readline()
    print(two,end='')
    three = file.readline()
    print(three,end='')