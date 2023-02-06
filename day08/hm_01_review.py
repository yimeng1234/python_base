"""
需求：设计 SweetPotato 地瓜类
1. 地瓜有两个属性：
    状态 state：初始状态为'生的'
    烧烤总时间 cooked_time：初始时间为0

2. 实现__str__方法，打印对象，输出：地瓜状态为：xxx, 烧烤总时间为：yyy 分钟
3. 定义 cook 方法, 形参为 time，传入本次烧烤时间
    1. 使用 烧烤总时间 对 本次烧烤时间 进行 累加，得到最新烧烤时间
    2. 根据 烧烤总时间, 设置地瓜的状态：
        0 <= 烧烤总时间 < 3 ： 生的
        3 <= 烧烤总时间 < 6 ： 半生不熟
        6 <= 烧烤总时间 < 8 ： 熟了
        大于等于8 ： 烤糊了
4. 创建对象，调用方法，验证结果
"""
class SweetPotato:
    def __init__(self,state="生的",cooked_time=0):
        self.state = state
        self.cooked_time = cooked_time
    def __str__(self):
        return f'地瓜状态为：{self.state} 烧烤总时间为：{self.cooked_time} 分钟'
    def cook(self,time):
        self.cooked_time += time
        if self.cooked_time >= 0 and self.cooked_time < 3:
            self.state = '生的'
        elif self.cooked_time >= 3 and self.cooked_time < 6:
            self.state = '半生不熟'
        elif self.cooked_time >= 6 and self.cooked_time < 8:
            self.state = '熟了'
        else:
            self.state = '糊了'
                
# 1
one = SweetPotato()
print(one)
one.cook(5)
print(one)
one.cook(5)
print(one)
print('*'*20)

# 2
two = SweetPotato(state='半生不熟',cooked_time=5)
print(two)
# 3
three = SweetPotato(state='熟了',cooked_time=7)
print(three)
