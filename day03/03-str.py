"""
字符串的定义
"""
str_1 = '我吹过你吹的' \
        '晚风'
str_2 = "那我们算不算相拥"

# 三个引号  内部其实是可以换行的
str_3 = '''你说啥呢'''
str_4 = """鹅鹅鹅
 
曲线向天歌"""

# 打印类型
print( type(str_3) )
print(str_1)
print(str_4)

# 单引号 和 双引号 可以嵌套
# i am Tom   I'm Tom
str_5 = "I'm Tom"
print(str_5)

# 单引号 和 双引号 不能串用
# str_6 = ' i hava a dream "

# I'm Tom
# 我们可以使用 转义的 斜杠（\）
str_6 = 'I\'m Tom'
print(str_6)

# 我们想 把字符串的 \n 原样输出
str_7 = "i \\n hava \\n a \\n dream"
# raw 原样的
str_8 = r"i \n hava \n a \n dream"
print(str_8)

# 路径
# 添加r的目的 就是  原样输出。
# 如果不添加r \+字母 【\n \t】 拥有特殊的用法
path = r"C:\Users\Ricky\Desktop\41\大纲5.1"
print(path)


