# 创建一个列表
l = [1,2,3,4,5,6,7,8,9,10]

# 定义一个函数，用来检查一个任意的数字是否是偶数。
def fn2(i) :
    if i % 2 == 0 :
        return True

    return False    

# 这个函数用来检查指定的数字是否大于5
def fn3(i):
    if i > 5 :
        return True    
    return False
# 这个函数可以将3的倍数取出
def fn4(i):
    if i % 3 == 0 :
        return True
    return False

def fn(func , lst) :# 定义高阶函数fn

    # 创建一个新列表
    new_list = []

    # 对列表进行筛选
    for n in lst :
      new_list.append(n)
    # 返回新列表
    return new_list
#此时就可以随意调用不同的函数来获得不同的结果了，
#只需要改变高阶函数fn的两个参数即可。     
print(fn(fn4 , l))#此时调用的是fn4，列表是l，即意味着取出l列表中所有能被3整除的数。
