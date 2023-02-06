# 1. 导入 pytest
import pytest
# 2. 定义一个 函数 求2个数的和
def add(x,y):
    return x + y
# 3. 定义测试用例类
class TestAdd:
    # pytest 的参数化代码
    # @pytest.mark.parametrize(拆包的字符串变量,参数化的数据列表)
    # parametrize(拆包的字符串变量,参数化的数据列表)
    # 本质 可以理解为 对 参数化的列表数据进行遍历
    # 遍历过程中，拿到 每一项的数据 进行拆包
    # a,b,expect = (1,1,2)
    @pytest.mark.parametrize('a,b,expect' , [(1,1,2),(0,1,1),(0,0,0),(-1,0,-1)])
    def test_add(self,a,b,expect):
        result = add(a,b)
        assert result == expect

"""
注意事项：
1. @pytest.mark.parameterize(拆包的字符串变量,参数化的数据列表)
2. 拆包的字符串变量-- 类型是字符串 里边的变量名 要用逗号进行分割。 字符串变量名要和方法的参数一致
3. 参数化的数据列表 -- 一般是列表 列表中 包裹 元组。 一个元组 表示 一个用例的数据。 用例的数据 一定要和 拆包的字符串变量对应
        [(),(),()] 
4. 参数化的方法，也要 设置   拆包的字符串变量
"""
# 4. 执行测试用例
# 方式1 在终端中使用 pytest -s 脚本名字