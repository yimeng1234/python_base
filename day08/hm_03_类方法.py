"""
语法：
class 类名：
    @classmethod
    def 方法名（cls）:
        pass

1. 类方法需要借助于 @classmethod 装饰器 来装饰
2. 类方法的第一个参数是 cls . cls 代表 类名   习惯都使用 cls
3. 类方法 其实主要就是为了 我们方便调用 类属性
    类属性的调用  类名.类属性    cls.类属性
4. 调用类方法 推荐使用 类名.类方法（）
"""
class Tool:
    #定义一个类属性  --> 归类所有
    count = 0
    # 初始化方法  对象属性 --> 归具体的对象所有
    def __init__(self,name):
        self.name = name
        # 我们需要统计 创建了多少工具对象
        Tool.count += 1
    # 定义一个类方法
    @classmethod
    def show_tool_count(cls):
        # cls 既然代表类名 我们使用 类属性 就可以使用 cls.类属性
        print(cls.count)
# 对象属性
one = Tool(name='铁锹')
two = Tool(name='扫把')
print(Tool.count)
#调用 类方法   类名.类方法
# 类名后边没有小括号
Tool.show_tool_count()

"""
面向对象 -->  类 和 对象 

通过类 创建一个 对象                     人民          你，我，他

对象属性  和 对象方法                    你，我，他 --钱， eat(),sleep()

类  Person,Animal,Login,Pay  
类属性 和 类方法                          人民的钱     代表人民消灭你

"""