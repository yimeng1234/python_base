
"""
1.
家具(HouseItem) 有 名字 和 占地面积，其中
– 席梦思(bed) 占地 4 平米
– 衣柜(chest) 占地 2 平米
– 餐桌(table) 占地 1.5 平米
类的设计
类名： HouseItem
属性： name,area
方法：__init__
     __str__
"""
class HouseItem:
    #初始化方法
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return f'家具名字 {self.name} 占地面积 {self.area}'
"""
2.
房子(House) 有 户型、总面积 和 家具名称列表
– 新房子没有任何的家具
打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表
家具 添加 到 房子 中

total 总计    free 剩余 
类名： House
属性： type,total_area,free_area,item_list
方法：   __init__（） 和 __str__()
        add_item()
"""
class House:
    def __init__(self,type,total_area):
        self.type = type                # 户型
        self.total_area = total_area    # 总面积
        self.free_area = total_area     # 针对于 新房子 总面积 就是剩余面积  因为新房子没有家具
        self.item_list = []             # 针对于 新房子 没有家具 。初始化一个 空列表
    def __str__(self):
        return f'户型:{self.type}、总面积:{self.total_area}、剩余面积:{self.free_area}、家具名称列表:{self.item_list}'
    # 家具放到家里
    # 既然我们需要将家具放到家里，必须给我们的方法，设置一个形参
    # 这个形参 是代表  家具的实例对象
    def add_item(self,item):
        # item = bed
        # 1. 判断 剩余面积 是否能够存放家具
        #  if 300 >= 4
        # item.属性
        if self.free_area >= item.area:
            # 2. 如果能够存放。把家具名字放入家具列表中。应该让剩余面积减少
            # bed.name
            # item.name
            self.item_list.append(item.name)
            #应该让剩余面积减少
            self.free_area = self.free_area - item.area
        else:
            # 3. 如果不能存放，打印 不能存放
            print("不能存放")

# 3. 将以上三件 家具 添加 到 房子 中
if __name__ == '__main__':
    #创建3个对象实例
    bed = HouseItem('席梦思',4)  # 位置参数
    chest = HouseItem(name='衣柜',area=2)  #关键字参数
    table = HouseItem('餐桌',area=350)    # 混用
    print('*'*30)
    home = House(type='别墅',total_area=300)
    print(home)
    print('1' * 30)
    # 对象.方法名（实参）
    home.add_item(bed)
    print(home)

    print('2' * 30)
    home.add_item(chest)
    print(home)

    print('3' * 30)
    home.add_item(table)
    print(home)