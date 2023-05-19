def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("请输入一个数: "))
print(num,"的阶乘是",factorial(num))
