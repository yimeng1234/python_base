"""
前提条件是 我们已经安装成功了 pytest

pytest 的使用步骤：
1. 定义测试用例类
    类要以 Test开头
    方法要以 test 开头
2. 执行测试用例
"""
import pytest

def add(x,y):
    return x + y

class TestAdd:
    # 用例1
    def test_add_01(self):
        result = add(1,1)
        print("我们一起学猫叫 一起喵喵")
        print(result)
    # 用例2
    def test_add_02(self):
        result = add(1,0)
        print(result)
if __name__ == '__main__':
    # 1. 导入 pytest    import pytest
    # 2. 借助于 pytest.main()
    #       main括号里是 列表
    #       列表是 第一个参数是 -s    -s可以把我们的print 打印显示在控制台
    #              第二个参数 就是 要运行的 脚本名 要有后缀名
    pytest.main(['-s','hm_09_pytest入门.py'])