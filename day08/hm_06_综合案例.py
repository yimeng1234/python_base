"""
类的设计
类名： Game
属性 ： 对象属性和类属性
    top_score
      player_name
方法： 对象方法、类方法、静态方法
    __init__
    __str__
    show_help()
    show_top_score()
    start_game()
创建对象
"""
class Game:
    top_score = 0  #类属性
    # 实例属性
    def __init__(self,player_name):
        self.player_name = player_name
    @staticmethod   # 静态方法
    def show_help():
        print('*'*20)
        print("① 查看帮助信息")
        print("*"*20)
    @classmethod  # 类方法
    def show_top_score(cls):
        # 类名.类属性  cls.类属性
        print(f'历史最高分是{cls.top_score}')
    def start_game(self): # 实例方法
        print("开始游戏")
        print("游戏结束")
if __name__ == '__main__':
    # 1.查看帮助信息 -- 调用静态方法
    Game.show_help() # 语法： 类名.静态方法()
    # 2.查看最高分
    Game.show_top_score() # 语法： 类名.类方法()

    # 3.创建对象
    xiaoming = Game(player_name='小明')
    # 调用： 对象方法
    # 语法： 对象变量名.对象方法()
    xiaoming.start_game()
    # xiaoming玩了最高分 100
    # 修改 最高分 修改 类属性
    Game.top_score = 100
    Game.show_top_score()
    # 4. 小美
    xiaomei = Game(player_name='小美')
    Game.top_score = 666
    Game.show_top_score()