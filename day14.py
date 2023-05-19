import random
import time

# Generate random Chinese characters
chinese_characters = "".join(random.sample(['我', '爱', '你', '是', '我', '生', '命', '中', '最', '重', '要', '的'], 8))

print("请输入下列字符串：", chinese_characters)

# Record the start time
start_time = time.time()

# Get the user input
user_input = input()

# Record the end time
end_time = time.time()

# Compare the user input with the original string
if user_input == chinese_characters:
    print("输入正确！")
else:
    print("输入错误！")

# Calculate the user time
user_time = end_time - start_time
print("你用时: ",user_time,"秒")
