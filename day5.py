s = input("Enter a string: ")

# 使用 isalpha() 分离出字母和数字
letters = [c for c in s if c.isalpha()]
numbers = [int(c) for c in s if c.isdigit()]

# 对字母和数字分别排序
letters.sort()
numbers.sort()

# 合并字母和数字
result = ''.join(letters + [str(n) for n in numbers])

print(result)
