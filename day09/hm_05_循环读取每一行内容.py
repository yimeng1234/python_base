# while True:
#    那一行 没内容 就停止循环
with open('data.txt','r',encoding='utf-8') as f:
    # 一行的读取
    while True:     # 死循环 因为我们也不知道会有多少行内容
        content = f.readline()      # 读取每一行

        if content:
            # 根据每一行的内容作为布尔值进行判断  非0 为True
            # content 只要有内容 就是 真True
            # content 没有内容 就是 假 False
            print(content)
        else:
            break                   # 没有内容就停止循环

print('后续代码')