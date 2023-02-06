# 1. 导入pytest
import pytest
# 2. 定义2个数的和 函数
def add(x,y):
    return x + y
# build 构建
def build_data():
    data = [
        (1,1,2),
        (1,0,1),
        (0,1,1),
        (1,1,3),        #错误的
    ]
    # return 返回数据
    return data
# 3. 定义测试用例类
class TestAdd:
    # build_data() 当调用函数的时候 可以读取数据
    # 一定要记得 函数后边添加小括号 来调用
    @pytest.mark.parametrize('a,b,expect' , build_data() )
    def test_add(self,a,b,expect):
        result = add(a,b)
        assert result == expect
# 4. 执行测试用例
# 方式1： 在终端中 输入 pytest -s 脚本名