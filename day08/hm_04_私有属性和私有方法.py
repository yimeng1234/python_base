"""
私有属性和私有方法：
        私有属性和私有方法 只允许在类的内部使用，不允许在类的外部使用

    都是两个连续的下划线
私有属性语法：
    定义：  __属性 = 数据值
    类的内部使用：   对象私有属性 self.__属性   类私有属性  cls.__属性

私有方法语法：
    定义：  __方法名
    类的内部使用：  对象方法：  self.__方法名（）    类私有方法  cls.__方法名（）
"""
"""
类名： Girl
属性： name,__age
方法： __ask_age(self)
"""
class Girl:
    def __init__(self,name,age):
        self.name = name        # 正常的
        self.__age = age        # 私有的属性
    # 私有方法
    def __ask_age(self):
        print("私有方法：你的年龄是多大")
    # 公开的方法
    def public_ask(self):
        print("能问年龄吗？")

    # 公开的方法
    def private_say(self):
        # 在方法的内部，调用私有属性、私有方法
        print(f'{self.name}年龄是{self.__age}')
        # 在类的内部，如何调用其他方法呢？ 例如私有方法
        self.__ask_age()

# 创建对象实例
xiaomei = Girl(name='小美',age=18)
# 私有的属性和方法 不能在类的外部访问
# print(xiaomei.__age)
# xiaomei.__ask_age()

#调用公开的方法
xiaomei.private_say()