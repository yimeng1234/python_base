import json     # 0. 导入 json
# 1. 有JSON形式的数据   -- 字典
json_dict = {
    'name':'如花',
    'age':28,
    'sex':False,
    'address':None,
    'boy_friend':['jack','rose']
}

# 2. 借助于 文件操作写入
with open('write.json','w',encoding='utf-8') as f:
    # json.dump(字典数据，文件变量)   ensure_ascii=False 中文可以按照文字的形式显示
    json.dump(json_dict,f,ensure_ascii=False)