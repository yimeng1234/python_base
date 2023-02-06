"""
需求：
1. 参考TPshop项目的登录功能（登录时需要输入用户名、密码、验证码），至少设计3条测试用例
2. 要求1：定义变量保存测试数据（包括不同测试数据对应的测试结果）
3. 要求2：至少写出3种以上不同的数据格式
4. 要求3：遍历测试数据并打印到控制台，数据格式“用户名：xxx 密码：xxx 验证码：xxx 期望结
果：xxx”
"""
# 用户名、密码、验证码
# 字符串   用户名-密码-验证码  字符串的分割

#1 列表
login_data = [
    ['13312345678','abcdef','8888','success'],        #  item
    ['13312345670','abcdef','8888','failed'],        #  item
    ['13312345678','123','8888','failed']            #  item
]
for item in login_data:
    # print(item)
    # item = ['13312345678','abcdef','8888']
    print(f'用户名：{item[0]} 密码：{item[1]} 验证码：{item[2]} 期望结果：{item[3]}')
print('*'*50)
#2 元组   -- 列表的区别 就是不能修改。用法和列表一致
login_tuple = (
    ('13312345678','abcdef','8888','success'),
    ('13312345670','abcdef','8888','failed'),
    ('13312345678','123','8888','failed')
)
for temp in login_tuple:
    # print(temp)
    print(f'用户名：{temp[0]} 密码：{temp[1]} 验证码：{temp[2]} 期望结果：{temp[3]}')
#3. 字典
print('$$$'*30)
login_dict = [
    {"name":"13312345678","password":"abcdef","code":8888,"expect":"success"},
    {"name":"13312345670","password":"abcdef","code":8888,"expect":"failed"},
    {"name":"13312345678","password":"123","code":8888,"expect":"failed"}
]

# 最外层的遍历 和上边一样

for dict_item in login_dict:
    # dict_item = {"name":"13312345678","password":"abcdef","code":8888,"expect":"success"}
    # end="" 就是为了 print不换行
    print(f'用户名：{dict_item.get("name")} 密码：{dict_item.get("password")}',end='')
    print("验证码：{} 期望结果：{}".format(dict_item['code'],dict_item['expect']))

