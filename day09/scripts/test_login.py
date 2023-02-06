
class TestLogin:   # 符合要求
    def test_login_01(self):
        print('01')

    def test_login_02(self):
        print('02')

    def it_login_02(self):
        print('03')


class ITLogin:  # 不符合要求
    def test_login_01(self):
        print('04')

    def test_login_02(self):
        print('05')