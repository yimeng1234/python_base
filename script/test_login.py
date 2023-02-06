
from service.login_service import login
# 运行 test_login.py 的时候
# login_sercie.py的 __name__ 的值是 login_sercie
# login_service != __main__
# 所以 if里的代码 不执行！！！

# 组织测试数据
# 正向
login('admin','123456',8888)
# 复制某一行 是光标在那一行，然后使用 ctrl + D 快捷键
# 反向的数据
login('lalala','123456',8888)
login('admin','ppt',8888)
login('admin','123456',9999)
