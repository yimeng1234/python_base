# common 公共的 共有的
# sayhi
def sayhi():
    print("hello")

# sayhi()
# 现在的一个情况是
# 单独运行 common.py 模块 会执行函数
# common.py模块 被其他模块 导入了 也会执行 函数

# 期望的效果是： 只是在 我单独运行 common.py模块的时候，执行函数

#两个连续的下划线[__] 前后边都是2个
# __name__  在使用的时候，其实就是2个值
# 1. 我们单独运行 这个模块的时候 __name__ 的值 就是 __main__  【两个连续的下划线】
# 2. 这个模块，被其他文件导入的时候 __name__的值 就是 模块名
print( __name__ )
if __name__ == '__main__':
    sayhi()