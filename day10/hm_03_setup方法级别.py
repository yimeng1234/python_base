#导包
import pytest

class TestBus:
    # 方法必须是 setup
    # setup 是方法级别  在每个用例方法调用前
    # 会自动调用这个方法
    def setup(self):
        print("上车 刷卡")
    # 方法必须是 teardown
    # teardown 是方法级别 在每个用例方法调用后
    # 会自动调用这个方法
    def teardown(self):
        print("下车 刷卡")

    # 以test 开头的 用例方法
    def test_on_607(self):
        print("在607上")
    def test_on_355(self):
        print("在355上")


# 方式1 直接在 终端中 使用 pytest -s 文件.py
# 方式2 if __name__ == '__main__'
if __name__ == '__main__':
    # pytest.main(列表)
    # 列表的第一个元素是 -s 表示 在终端中显示 打印的信息
    # 列表 的第二个元素 是 模块名 必须添加 后缀
    pytest.main(['-s','hm_03_setup方法级别.py'])