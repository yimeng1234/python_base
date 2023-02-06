# 方式1
# import 模块
import demo

# 使用 模块.变量名 / 模块.函数名()
print(demo.num)
print('*'*50)
a = demo.get_2_sum(1,1)
print(a)
print('*'*50)

# 方式2
# from ... import ..
# 意思就是 从 demo模块 导入一个 num
from demo import num
from demo import get_2_sum
# 或者 一起导入
from demo import num,get_2_sum

# 使用  直接使用 变量名 / 函数名
print(num)


#######################
print("$$$"*20)

import random
# 1~10
print(random.randint(1,10))

# 模块可以起别名
# 作用 就是 针对于 比较长的名字可以改短
from demo  import get_2_sum as get_sum

import random as r

print(r.randint(1,10))