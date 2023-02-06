
class Game:
    # 类属性  记录最高分
    top_score = 0
    def __init__(self,player_name):
        # 对象属性[实例属性]    每一个对象 都有 player_name
        self.player_name = player_name
    # 静态方法  第一个参数没要求
    @staticmethod
    def show_help():
        print("显示帮助信息")
    # 类方法   第一个参数是cls  代表类名
    @classmethod
    def show_top_score(cls):
        print(f"最高分是{cls.top_score}")
    # 对象方法[实例方法]  第一个参数是 self
    def start_play(self):
        print("玩游戏")





if __name__ == '__main__':
    Game.show_help()        # 推荐语法： 类名.方法名（）
    Game.show_top_score()   # 推荐语法： 类名.方法名（）
    xiaoming = Game(player_name='小明')
    xiaoming.start_play()   # 对象变量名.方法名（）

    print('*'*20)
    xiaoming.show_help() # 不推荐： 对象变量名.静态方法()
    print("#"*20)
    xiaoming.show_top_score()  # 不推荐： 对象变量名.类方法（）
    print('!'*20)
    #Game.start_play()       # 错误！！！ 类名.对象方法（）