# 1. 家具
class HouseItem:
    def __init__(self,name,area):
        self.name = name        #家具名称
        self.area = area        #家具占用面积
# 2. 房子
class House:
    def __init__(self,type,total_area):
        self.type = type        #房子类型
        self.total_area = total_area    #房子总面积
        self.free_area = total_area     #房子剩余面积
        self.item_list = []             #房子的家具列表
    def add_item(self,item):
        if self.free_area > item.area:  #剩余面积 大于 家具面积
            self.item_list.append(item.name)    # 列表添加数据
            self.free_area = self.free_area - item.area #让剩余面积 减少
        else:
            print("家具放不下了")
    def __str__(self):
        return f'剩余面积是 {self.free_area} 家具列表{self.item_list}'
# 3. 实例化对象
# 将实例化的家具 放到 实例化的房子里
if __name__ == '__main__':
    bed = HouseItem(name='床',area=4)  # 床
    # bed.area  bed.name
    chest = HouseItem(name='衣柜',area=2)# 衣柜
    # 餐桌
    table = HouseItem(name='餐桌',area=400)
    #房子
    home = House(type='别墅',total_area=300)

    home.add_item(bed)  # 添加床
    print(home)
    print('*'*30)

    home.add_item(chest)    # 添加衣柜
    print(home)
    print('!'*30)

    home.add_item(table)    #添加餐桌
    print(home)














