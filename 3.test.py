
#输入公交卡当前的余额，只要超过两元，就可以上车，如果车上有空座就可以坐下
ye = eval(input("请输入你的公交卡余额"))
zw = 1
if ye >= 2:
    print("可以上车")
    if zw == 1:
        print("你可以坐下")
else:
    print("不可以上车")

i = 0
while i<5:
    print("第%d次" % (i + 1 ) )
    print("你好世界")
    i += 1

#计算1~100的累积和（包含1和100）
num = 1
my_sum = 0
while num < 101:
    my_sum += num
    num += 1
print("1~100求和结果时%d" %my_sum)