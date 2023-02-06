
#1.导入系统的模块 json
import json
# 2. 文件读操作
with open('data.json','r',encoding='utf-8') as f:
    # 3.json.load(文件变量)  已经讲JSON数据转换为我们的Python数据格式
    data = json.load(f)
    #class 'dict'
    print(data)
    print( type(data) )
    # 获取name
    print( data.get('name') )
    print( data['boy_firend'] )
    print( data['address'] )