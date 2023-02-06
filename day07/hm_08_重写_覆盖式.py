# 动物
class Animal:
    def eat(self):
        print("吃")

# 猫
class Cat(Animal):
    # 覆盖式 重写 就是相当于 写一个和父类同名的方法
    def eat(self):
        print("吃鱼 吃大鱼 吃鲨鱼")

# 创建一个猫的对象
c = Cat()
c.eat()