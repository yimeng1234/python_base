"""
办一张公交卡

上2路公交车
    上车刷卡
    下车刷卡

上3路公交车
    上车刷卡
    下车刷卡

注销公交卡

数据库查询
    连接数据库
    关闭数据库

数据库的新增
    连接数据库
    关闭数据库
"""
class TestBus:
    # up 上
    def up(self):
        print("上车刷卡")
    # down 下
    def down(self):
        print("下车刷卡")
    #坐车
    def test_on_607(self):
        #调用 上车刷卡  up方法
        # 在类的内部 调用 方法 使用 self.方法名（）
        self.up()
        print('我在 607上')
        self.down()
    def test_on_355(self):
        self.up()
        print('在 355 公交上')
        self.down()