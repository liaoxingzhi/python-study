# @time : 2022/6/7 21:04
# @author : Freya
# File : 九九乘法表

for i in range(1, 10):
    # 每次外循环开始打印空格1~9
    print()
    for j in range(1, i + 1):
        # end=' ':每次内循环以end里面的内容连接
        print(j, '*', i, '=', j * i, end='  ')

