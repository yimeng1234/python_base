# a=100，b=200，定义一个匿名函数，求出a*b的值
# count = lambda a,b:a * b
# result = count(100,200)
# print(result)
# 12按照以下要求封装一个函数：
# 1.提示用户输入一个整数
# 2.判断数字的类型，如果是偶数打印“xx是偶数”，否则打印“xx是奇数”

# def count01():
#     test1 = int(input("请输入一个整数:"))
#     while True:
#         if test1 % 2 == 0:
#             print(f"{test1}是偶数")
#             break
#         else:
#             print(f"{test1}是奇数")
#             break
#     return test1
# #
# aaa = count01()

# 13编写一个函数，求1到100之间的奇数和
# def count2():
#     num = 0
#     for i in range(101):
#         if i % 2 != 0:
#             num += i
#         # i += 1
#     return num
#
# aaa = count2()
# print(aaa)
print(sum(range(1, 100, 2)))
# 按要求编写json文件，并通过程序读取文件内容。
#
# 需求：小明是个男生，今年20岁了，毕业于清华大学，家里养的宠物有1岁的狗、
# 2岁的猫、3岁的猪，他的幸运数字是2、5、8。
# 请把上面的信息用JSON数据来表示，并保存到data.json文件中。
# 要求：
#     1.使用UnitTest框架编写测试脚本
#     2.读取json文件，并打印出姓名和学校名称
#     3.断言姓名是否等于"小明"，断言学校名称中是否包含"清华"
import json
import pytest

json_data = {
    "name": "小明",
    "max": "男生",
    "age": 20,
    "school": "清华大学",
    "home_animal": ['1岁的狗', '2岁的猫', '3岁的猪'],
    "lucky_num": [2, 5, 8]
}


class JDAdd:
    def jd_test_json_add(self):
        with open('../data.json', 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False)

    def jd_test_json_read(self):
        with open('../data.json', encoding='utf-8') as b:
            data = json.load(b)
            data1 = data.get('name')
            data2 = data.get('school')
        assert data1 == '小问问', '名字不对哦'
        assert '橘子' in data2, '学校错了哦'


if __name__ == '__main__':
    pytest.main(['-s', 'jd_work.py'])
