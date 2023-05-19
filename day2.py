#判断闰年
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year = int(input("请输入年份呢: "))
if is_leap_year(year):
    print(year, "是闰年")
else:
    print(year, "不是闰年")
