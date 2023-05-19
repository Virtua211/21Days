count = 0
result = ""
for i in range(500, 2023):
    if i % 6 == 0 and i % 10 == 2:
        count += 1
        result += str(i) + " "
print(result)
print("共有{}个数字符合条件".format(count))
