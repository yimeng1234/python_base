# 1. 定义一个Dog类
class Dog:
    def game(self):
        print("普通狗只是简单的玩耍")
# 2. 定义一个 哮天犬类
class XiaoTianDog(Dog):     # 这里需要继承
    def game(self):
        # 覆盖式重写
        print("哮天犬 需要在天上玩耍")
# 3. 定义一个 Person类
class Person:               # 这里需要
    def play(self,dog):
        # dog = d
        # d.game()
        dog.game()





# 创建对象
# 狗狗1
d = Dog()
# 狗狗2
xtq = XiaoTianDog()
# 人的实例对象
xiaoming = Person()
# 人和狗狗玩

xiaoming.play(d)
print('*'*30)
xiaoming.play(xtq)

