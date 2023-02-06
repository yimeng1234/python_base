
# 1. 如果 写入的文件 不存在，系统会自动给我们创建新文件写入
# 2. 如果 写入模式是 w， 文件已经存在了，则 覆盖写入
# 3. 如果想给已经存在的文件追加 则使用 ‘a’   # append 追加
# mode 是w 表示写入
# with open('new.txt','w',encoding='utf-8') as f:       # 覆盖式写入
with open('new.txt','a',encoding='utf-8') as f:         # 追加
    # f.write(字符串)   不会自动换行，如果需要我们自己在字符串中添加 转义字符
    f.write('abc\n')
    f.write('xyz\n')
    f.write('p\tp\tt')