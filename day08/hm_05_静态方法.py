"""
静态方法什么时候使用呢？？？
我们既不需要 使用 对象属性 或者 对象方法      对象方法第一个参数是self
也不需要 使用 类属性 或者 类方法              类方法的第一个参数是 cls
的时候
可以定义一个 静态方法
例如：  我就是定义一个 说明书

class 类名:

    @staticmethod
    def 方法名(参数列表):
        pass

1. 类方法 使用 @staticmethod 装饰器 装饰
2. 类方法 没有默认参数。
3. 类方法调用 使用 类名.静态方法
"""
# 有一个游戏， 调用一个方法 实现 游戏说明
class Game:

    @staticmethod
    def intro():
        print("*"*20)
        print("欢迎来到吃鸡的世界")
        print("左边按钮 用于控制方法")
        print("右边按钮 用于出击")
        print("大吉大利 今晚吃鸡")
        print("*"*20)

# 调用
# 类名.静态方法  类名后边不需要小括号
Game.intro()
