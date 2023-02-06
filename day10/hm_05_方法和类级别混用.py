"""
办一张公交卡

    上车刷卡
    607
    下车刷卡

    上车刷卡
    355
    下车刷卡

注销一张公交卡
"""
import pytest
# 强调一点： 不管是类级别还是方法级别的方法 按需使用
class TestBus:
    #类级别
    # 在所有的对象方法执行前 调用一次
    def setup_class(self):
        print("办一张公交卡")             # 连接数据库
    # 在所有的对象方法执行后 调用一次
    def teardown_class(self):
        print("注销一张公交卡")            # 关闭数据库连接

    #方法级别
    # 在每一个对象方法执行前 都会执行
    def setup(self):
        print("上车刷卡")               # 新增测试数据
    # 在每一个对象方法执行后 都会执行
    def teardown(self):
        print("下车刷卡")               # 把新增的测试数据删除

    # 对象方法
    def test_on_607(self):
        print("607")

    def test_on_355(self):
        print('355')

# 方式1： 在终端中 输入 pytest -s 脚本名字 要有后缀
# 方式2  在 __name__ == '__main__' 中 pytest.main([-s,脚本名字【有后缀】])
if __name__ == '__main__':
    # pytest.main(列表)
    # 列表的第一个参数是  打印信息
    # 列表的第二个参数是 脚本名字 要有后缀
    pytest.main(['-s','hm_05_方法和类级别混用.py'])




