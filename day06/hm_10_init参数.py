# 定义一个类
class Cat():
    # 初始化方法 -- 只要我们创建实例对象 就会自动调用
    def __init__(self,name):
        # 在初始化方法上，添加参数
        # 我们在创建对象的时候，就需要给这个参数 传值
        # self.属性 = 形参
        # 一般情况下 我们都设置 属性名和形参名 一致
        self.name = name
    def eat(self):
        print(f'{self.name} 吃鱼')
    def drink(self):
        print(f'{self.name} 喝水')
# 创建实例对象
# 在创建实例化对象的时候， 要给 name赋值
tom = Cat(name='tom')
#添加一个属性
# 实例对象变量名.属性名=数据值
# tom.name = 'tom'
tom.eat()
tom.drink()

# 对象2
jack = Cat(name='jack')
jack.eat()
# 对象3
rose = Cat(name='rose')
rose.eat()
