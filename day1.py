# 输出指定范围内的素数
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes(start, end):
    for i in range(start, end + 1):
        if is_prime(i):
            print(i)

# 获取用户输入的范围
start = int(input("请输入起始数字："))
end = int(input("请输入终止数字："))

# 输出素数
print_primes(start, end)

