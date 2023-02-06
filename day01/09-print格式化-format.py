name = '张三'
age = 20
address = '北京中南海旁边的小桥下'
# 我的名字是 xxx ,我今年 xxx 岁，我住在 xxx
# format的语法形式
# ' {}    {}    {}   '.format(变量名，变量名，变量名)
# 1. {} 是表示一个占位符   最终会被 format 对应位置的 变量值 代替
# 2. {} 的数量要和 format后边的变量名 数量 一致
print('我的名字是{}，我今年{}岁，我住在{}'.format(name,age,address))