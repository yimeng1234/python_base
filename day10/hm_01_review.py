"""
pytest 基本使用步骤：
1. 定义测试用例类。
    类必须以Test开头
    类中的方法必须以 test开头
2. 运行测试用例类。
    在终端中 使用 pytest -s python文件  【推荐】
    需要使用 pytest.main()
"""
import pytest
def add(x,y):
    return x + y

class TestAdd:
    def test_01(self):
        result = add(1,1)
        print(result)

    def test_02(self):
        result = add(1,0)
        print(result)

if __name__ == '__main__':
    pytest.main(['-s','hm_01_review.py'])