# 1. 导入pytest
import pytest

# 2. 定义一个函数 求2个数的和
def add(x,y):
    return x + y        # 记得添加return
# 3. 定义测试用例类
class TestAdd:
    def tet_add_01(self):
        # 1,1,  2
        result = add(1,1)
        #断言
        assert 2 == result

    def tet_add_02(self):
        # 0,1   1
        result = add(0,1)
        assert 1 == result

    def tet_add_03(self):
        # 0,0   0
        result = add(0,0)
        assert  0 == result

    # 实现 代码和数据的分离
    def test_add(self):
        # 1.组织数据
        # 我们组织3组数据
        # 每一组的第一个数 和 第二个数 用于求和
        # 每一组的第三个数 用来判断
        data = [(1,1,2),(0,1,1),(0,0,0)]
        # 2.实现代码
        # 我们应该遍历data 来获取 每一组
        # for item in data:
            # item 代表着 一组数据
            # item = (1,1,2)
        # a,b,expect = (1,1,2)          expect 期望
        # a = 1   b = 1  expect= 2
        for a,b,expect in data:
            print(a,b,expect)
            # print('*'*20)
            result = add(a,b)
            assert expect == result
# 4. 执行测试用例类
if __name__ == '__main__':
    pytest.main(['-s','hm_07_参数化引入案例.py'])
