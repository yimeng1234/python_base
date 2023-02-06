
# 提示用户 输入密码
password = input("请输入密码：")
# 如果 长度少于 8，
if len(password) < 8:
    # 抛出 异常
    raise Exception('密码长度不够8位')
# 1. 抛出异常的关键字是 raise
# 2. raise 后边要有一个 空格
# 3. 空格后边跟 Exception 实例对象
# Exception(异常提示信息)
print('abc')
