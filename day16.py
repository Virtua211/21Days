n = int(input("输入一个数: "))
print( n,"的因数是:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
