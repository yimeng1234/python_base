print("hello world")
# 只要是以 .py结尾的 都是 模块
# 定义的变量
num = 666
# 定义的函数
def get_2_sum(num1,num2):
    result = num1 + num2
    #return 结果
    return result
    # print(result)
# 1. 自己会定义一些模块
# 2. 系统也会有自己的模块

#两个连续的下划线[__] 前后边都是2个
# __name__  在使用的时候，其实就是2个值
# 1. 我们单独运行 这个模块的时候 __name__ 的值 就是 __main__  【两个连续的下划线】
# 2. 这个模块，被其他文件导入的时候 __name__的值 就是 模块名
print(__name__)
