"""
需求：
1. 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
字符串变量 = input(提示字符串)
user = int( input("石头（1）／剪刀（2）／布（3）") )   2
2. 电脑随机出拳 —— 先假定电脑只会出石头，完成整体代码功能
computer = 1
3. 比较胜负

"""

# usre2 = int(input("请输入：石头（1）／剪刀（2）／布（3）") )
# import random
# user = int(input("石头（1）／剪刀（2）／布（3）：") )
# computer = random.randint(1,3)
# if (computer == 1 and user == 3) or (computer == 2 and user == 1) or (computer == 3 and user == 2):
#     print("用户赢了")
# elif computer == user:
#     print("平手")
# else:
#     print("输了")
# print(computer)
# alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
# def sort_by_age(list1):
#     # return sorted(alist,key=lambda x:x['age'],reverse=False)
#     return sorted(alist,key=lambda x:x['age'],reverse=True)
# print(sort_by_age(alist))
# import random
# from random import shuffle
#
# x = ["sadg","是否收到","事实上","111","222"]
# shuffle(x)
#
# print(x)
# aa = random.Random(5)
# print(aa)
# bbb = []
# aaa = [1,3,6,0,2,7]
# print(aaa[::-1])
# for i in aaa[::-1]:
#     # aaa.reverse()
# # for i in aaa:
#     print(i)
# a  出现的次数，和第五次出现的下标，不出现就输出-1
from itertools import count


x = [1,"2","a","a","a","a","a"]
b = 4
print("字母a出现的次数为{}次".format(x.count("a")))
for i in x:

    if i.index("a")== b:
        print(i)
    else:
        print("没有")


# print(count())
# for i in x:
#     if i == "a":
#         # i += b
#         print(f"第{i}次出现")
# #
# l = [1, 2, 3, 4, 7, 2, 5, 6, 2, 8, 9, 0]
# first = 0
# for i in range(l.count(2)):
#     new_l = l[first:]
#     index = first + new_l.index(2)
#     print
#     'find the index of 2:', index
#     first = index + 1











