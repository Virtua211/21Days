n=int(input('请输入一个三位的整数：'))
ge=n%10
shi=n//10%10
bai=n//100
sum=ge+shi+bai
print('整数各位数字之和是：',sum)