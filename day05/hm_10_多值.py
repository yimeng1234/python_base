"""
求n个数的和

针对于 参数 不确定的情况 可以使用 *args

"""
# 因为是求和， 至少也是求2个数的和。
# 所以我们定义了 num1 接收第一个
# 所以我们定义了 num2 接收第二个
# *args 接收 后续的参数
def get_n_sum(num1,num2,*args):
    # print(num1,num2)
    # args 是一个元组
    # 整数 + 元组
    # args 是元组 不能直接和 整数运算
    # args = (3,4,5)
    result = num1 + num2
    # 遍历 -- 就是 拿到容器的每一个元素
    for i in args:
        # 累加
        result = result + i
    # 我们应该在 对 args 遍历完成之后，再返回
    return result
# 调用
# get_n_sum(num1=1,num2=2)
# get_n_sum() 是有返回值的
# 变量名 = 有返回值的函数()
ret = get_n_sum(1,2,3,4,5,10,100)
print(ret)