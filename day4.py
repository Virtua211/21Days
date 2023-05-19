string = input("请输入字符串: ")

# 使用字典存储每个字符出现的次数
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# 找出重复字符
for char, count in char_count.items():
    if count > 1:
        print(f"字符 '{char}' 重复了 {count} 次")
