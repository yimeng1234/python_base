# 1. 导入pytest
import pytest
# 2. 定义一个函数 求2个数的和
def add(x,y):
    return x + y
# 定义一个变量
data = [
    (1,1,2),
    (1,0,1),
    (0,1,1),
    (0,1,0)
]
# 3. 定义测试用例类
class TestAdd:
    #@pytest.mark.parametrize( 用于解包的字符串变量名  ,  列表数据)
    @pytest.mark.parametrize('a,b,expect' , data)
    def test_add(self,a,b,expect):
        result = add(a,b)
        assert result == expect

# 4. 执行测试用例
# 方式2
if __name__ == '__main__':
    pytest.main(['-s','hm_09_参数化_方式2.py'])