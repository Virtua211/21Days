def gcd_and_lcm(a, b):
    if a > b:
        a, b = b, a
    while b % a != 0:
        b, a = a, b % a
    gcd = a
    lcm = int(a * b / gcd)
    return gcd, lcm

a = int(input("输入第一个数: "))
b = int(input("输入第二个数: "))

gcd, lcm = gcd_and_lcm(a, b)
print(f" {a} 和 {b} 最大公约数是: {gcd}")
print(f" {a} 和 {b} 最小公倍数是: {lcm}")
