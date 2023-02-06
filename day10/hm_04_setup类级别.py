# 导入pytest 以备后边使用
import pytest

# 定义用例类
class TestBus:
    # 类级别 就是 这个方法在这个类中
    # 只调用一次
    # 1. 方法名必须  setup_class
    # 2. 虽然叫做类级别方法 但是不需要使用 @classmethod装饰
    # 3. 这个方法在这个类中 所有的对象方法执行前 只调用一次
    def setup_class(self):
        print("办一张公交卡")
    # 1. 方法名 必须是 teardown_class
    # 2. 虽然叫做类级别方法 但是不需要使用 @classmethod装饰
    # 3. 这个方法在这个类中 所有的对象方法执行完成之后 只调用一次
    def teardown_class(self):
        print("注销公交卡")
    # 用例方法
    def test_on_607(self):
        print('在607上')
    def test_on_355(self):
        print("在355上")
# 方式1  在终端中 通过 pytest -s 脚本文件
# 方式2  在__name__ == '__main__'中 使用 pytest.main(['-s',脚本文件])