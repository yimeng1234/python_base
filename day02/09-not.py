"""
not 就是取反

True        not True ==> False
False       not False ==> True

"""
if False:
    print("gogogo")
if not True:
    print("gogogo")

# 1. 定义一个布尔型变量 is_employee，编写代码判断是否是本公司员工
# employee 员工
is_employee = False
# 2. 如果不是    提示不允许入内
# not False  ==> True
# not True   ==> False
if not is_employee:
    print("不允许入内")
