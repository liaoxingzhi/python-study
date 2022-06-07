# @time : 2022/6/7 21:04
# @author : Freya
# File : 九九乘法表

for i in range(1, 10):
    print()
    for j in range(1, i + 1):
        print(j, '*', i, '=', j * i, end='  ')
