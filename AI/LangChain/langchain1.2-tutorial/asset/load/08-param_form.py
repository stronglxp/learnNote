"""
三 函数参数形式
"""
# 1.位置参数
# 2.关键字参数
# 3.默认参数
# 4.不定长参数
# 4.1 带一个*
def printInfo(num,*vartuple):
    print(num)
    print(vartuple)

printInfo(70,60,50)

print("-" * 20)
# 如果不定长的参数后面还有参数,必须通过关键字参数传参
def printInfo1(num1,*vartuple,num) :
    print(num)
    print(num1)
    print(vartuple)

printInfo1(10,20,num = 40)

print("-" * 20)
# 如果没有给不定长的参数传参,那么得到的是空元组
printInfo1(70,num = 60)
# 4.2 带二个*
def printInfo(num,**vardict):
    print(num)
    print(vardict)
    # return

printInfo(10,key1 = 20,key2 = 30)