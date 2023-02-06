
# 求n个数的和
def get_n_sum(*args):
    # 定义一个 局部变量
    result = 0
    # args = (1,2,3,4,)
    # 遍历元组  -- 拿到元组中的每一个元素
    for i in args:
        result = result + i
    #应该是在 累加完成之后【for结束】 返回
    return result

#调用
# 元组的拆包
# data_tuple = 10,20,30,40,50
# 或者
data_tuple = (10,20,30,40,50)
# 元组的拆包 其实就是在元组变量名前边 添加 一个 *
ret = get_n_sum(*data_tuple)

print(ret)
