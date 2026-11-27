"""
二 函数参数
"""


# 1. 无参数版本 - 只能计算固定的购物车
def calculate_total_no_params():
    """计算固定购物车总价"""
    prices = [100, 50, 30]  # 商品价格固定写死在函数内
    total = 0
    for price in prices:
        total += price
    return total

# 只能计算一个固定的购物车
print(f"购物车总价:{calculate_total_no_params()}")

# 2.有参数版本 - 可以计算任意购物车
def calculate_total(prices):
    """计算任意购物车总价"""
    total = 0
    for price in prices:
        total += price
    return total

# 可以计算任意购物车
cart1 = [100, 50, 30]
cart2 = [200, 80, 45, 60]
cart3 = [75, 90, 120]

print("第一个购物车总价:{calculate_total(cart1)}:")
print("第二个购物车总价:{calculate_total(cart2)}")
print(f"第三个购物车总价:{calculate_total(cart3)}")


# 3.参数传递
# 3.1 不可变类型 函数传递不可变对象

def changeInt(a) :
    print("函数体中未改变前a的内存地址",id(a))
    a = 10   #底层会创建一个新对象 然后给新对象一个新值
    print("函数体中改变后a的内存地址",id(a))

a = 2 # 创建一个对象 然后给这个对象一个值
changeInt(a)
print(a)
print("函数外b的内存地址",id(a))



# 输出结果
# 函数体中未改变前a的内存地址 140729722661336
# 函数体中改变后a的内存地址 140729722661592
# 2
# 函数外b的内存地址 140729722661336


# 3.2 可变类型 函数传递不可变对象

def changeList(myList) :
    myList[1] = 50
    print("函数内的值",myList) # [1,50,3]
    print("函数内列表的内存",id(myList)) # 0111111

mlist = [1,2,3]  # 底层创建一个对象 地址0111111
changeList(mlist)
print("函数外的值",mlist) # # [1,50,3]
print("函数外列表的内存",id(mlist))

# 输出结果
# 函数内的值 [1, 50, 3]
# 函数内列表的内存 1380193079680
# 函数外的值 [1, 50, 3]
# 函数外列表的内存 1380193079680

