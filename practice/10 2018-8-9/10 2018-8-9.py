fpath='info.c'
f=open(fpath,'a+')#只能添加的 跳到0也写不进去
f.seek(0)
#f.close()
#f.flush()#刷新
#f.fileno()#用于os模块的read方法
#f.isatty()#判断链接到终端的文件
#next()#下一行
#f.read([size])#读取所有或指定字节
#f.readline([sizeint])#读取所有行或大于size的最小行数
#f.seek(offset[,whence])#移动文件指针
#f.tell()#获取文件操作指针位置
#f.truncate([size])#有size则从开始截取size个字符,否则从当前截取到末尾
#f.write(str)#写入一行 返回长度
#f.writelines(sque)#写入字符串列表
print(fpath)

def put_strs(arr):
	for i in arr:
		print('\''+i+'\'',end=' ')

arr=[]
ver=f.readline()
print('\''+ver+'\'',end='')
if(ver==''):
	print('file is empty')
	ver=0
	#exit()
else:
#	print('***********'+ver)
	ver=(int(ver)+1)
#	print('***********'+str(ver))
	print('*next()')
	print('\''+next(f)+'\'',end='')
	print('\''+next(f)+'\'',end='')
	print('*read()')
	print('\''+f.read(3)+'\'')
	print('*readlines()')
	a=f.readlines()
	put_strs(a)
	print(a)
	print('tell()',f.tell())
	
	while 1:
		i=input()
		if i=='':
			break;
		arr.append(i)
f.close()
f=open(fpath,'w+')
f.write(str(ver)+'\n')#不会回车
f.write('1,2,3,4\nasd\n2333')
f.writelines(arr)#也不会回车
f.close()


