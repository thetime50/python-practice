import os
#os 模块
def put_strarr(ar):
	for i in ar:
		print('\''+i+'\'')

put_strarr(dir(os))

#工作路径
start=os.getcwd()#命令行所在路径
print(start)
#print(os.getcwdu())#找不到??
os.chdir('..')
print(os.getcwd())
put_strarr(os.listdir('./'))
#fd=os.open('11  2018-8-11/note.c',os.O_RDONLY)
#os.fchdir(fd)
#os.close(fd)#找不到??
os.chdir(start)
print(os.getcwd())
#os.chroot('..')#找不到??
print(os.getcwd())

fd=os.open('test.c',os.O_RDWR|os.O_CREAT)
fu=os.dup(fd)
print(fd,fu)
os.write(fu,bytes("This is test",'utf-8'))

#os.fdopen(fd,'r+')
print(os.stat('test.c'))
print(os.fstat(fd))
#print(os.lstat())

print(os.isatty(1),os.isatty(fd))
#print(os.ttyname(1))#找不到??
os.close(fd)

put_strarr(os.listdir())
try:
	os.makedirs('123/45/6')
except:
	pass
input('next')
#os.mkdir()
try:
	os.rmdir('123/45/6')#如果目录为空则删除目录整个路径，非空没删除不报错
except:
	pass
open('123/t.c','w+').close()
input('next')
os.removedirs('123/45')#删除已存在的目录，没有目录成功，无法删除报错
#print(os.statvfs('123'))#找不到??
#for ro,dirs,files in os.walk('..'):#会遍历到子目录
#	print(ro,dirs,files,'\n')
for ro,dirs,files in os.walk('..',topdown=False):#先遍历子目录了
	print(ro,dirs,files,'\n')
#print(os.tcgetpgrp(1))#找不到??
