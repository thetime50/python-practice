#开始编程
a,b=0,1
while b<10:
	print(b,end=',')
	a,b = b,a+b#从左开始运算等号右边的表达式 运算结束后再对应赋值
print('')

#条件语句
#<	小于
#<=	小于或等于
#>	大于
#>=	大于或等于
#==	等于，比较对象是否相等
#!=	不等于
from random import *
#a=input('input a')
a=randrange(-1,2)
print('a is',a)
if a>0:
	print('a>0')
elif a<0:
	print('a<0')
else:
	print('a==0')