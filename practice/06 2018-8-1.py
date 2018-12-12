#循环语句
#while
#没有do

from random import *
i=randrange(1,11)
#j=int(input('input 1-10:'))
j=i
while j!=i:
	if j>i:
		print('input > i')
	else:
		print('input <i')
	j=int(input('input 1-10:'))
else:
	print('yes i='+str(i))#其实感觉有点迷 都是必须会执行的啊

while i>5: print(i,end=',');i=i-1#同if 语句只有一条时可以在同一行
else: print('end')#i=2还是会进来啊


#for语句
#便利序列 如列表或者字符串
li=[1,2,'123',(4),set(),3]
for i in li:
	print(i)
else:
	print('end',i)

for i in 'hello':
	print(i+'-',end='')
else:
	print('')

for i in range(0,len(li),2):
	print(li[i],end=' ')
print('')

#break 跳出for结构 不执行else
#continue

print('\n执行break 跳过else')
for i in [1]: break
else: print('this is break') 

print('\n通过判断退出循环 执行else')
for i in []: pass
else: print('this is break')



