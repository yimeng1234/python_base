
def money():
    print("给钱")

# 银行内部，这个钱 怎么数 都是内部的
# money()

print(  __name__ )
# __main__
# __main__ 单独运行模块的时候的值
# bank 其他模块导入它的时候
if __name__ == '__main__':
    money()