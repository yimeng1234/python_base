
# 1. 定义一个函数 计算2个数的和
def add(x,y):
    return  x + y
# 2. 定义测试用例类
class TestAdd:
    def test_add_01(self):
        result = add(1,1)
        # 借助于 断言
        # assert
        # assert 条件判断,提示信息
        # 1. assert 是关键字  后边要有空格
        # 2. 条件表达式为 True 表示用例通过
        #    条件表达式为 False 表示用例不通过
        # 3. 提示信息可以不用写
        assert True     # 表示满足期望 不会有提示发生 用例通过
        # if result == 2:
        #     print("通过")
        # else:
        #     print("不通过")
    def test_add_02(self):
        result = add(1,0)
        assert False,'计算结果不符合预期'   # 没有满足期望 断言发生  用例不通过

    def test_add_03(self):
        result = add(0,0)
        # assert 条件判断
        # == 才是判断
        assert result == 0

    def test_add_04(self):
        # 模拟一下
        # 定义一个变量 模拟接收提示信息
        msg = '用户名不能为空!'
        # in 是在 的意思
        # 字符串1  in  字符串2
        # 字符串2中 是否 包含 字符串1
        assert '用户名能' in msg , '用户名提示信息错误'
# 3. 执行测试用例类
# 方式1 在终端中 通过 pytest -s 脚本名