"""
需求：
1. 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
字符串变量 = input(提示字符串)
user = int( input("石头（1）／剪刀（2）／布（3）") )   2
2. 电脑随机出拳 —— 先假定电脑只会出石头，完成整体代码功能
computer = 1
3. 比较胜负

我们只需要把我们如何胜的情况记录下来     if    (条件1 and 条件2) or () or ()
user == compueter 是平的情况          elif  user == computer
剩下其他就是 负                        else

我们          电脑
3              1
1              2
2              3

"""
# 1. 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
user = int( input("石头（1）／剪刀（2）／布（3）:") )

# 2. 电脑出拳。暂时先让电脑为 1
# 2.1 导入 random
import random
# 2.2 设置随机数的开始和结尾
# 变量名 = 生成的随机数
computer = random.randint(1,3)
print(computer)

# 3. 比较
# 进行比较 一定是 2个等于号  1个等于号是赋值
# () 的优先级是最高的，他们相当于一个整体
if ( user == 3 and computer == 1) or ( user == 1 and computer == 2 ) or ( user == 2 and computer == 3):
    print("我们胜利了，走吃炸鸡去，喝啤酒")
elif user == computer:
    print("平局，不要走，决战到天亮")
else:
    print("电脑赢了，不玩了，砸了")