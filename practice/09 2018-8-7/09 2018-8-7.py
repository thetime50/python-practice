#IO
import sys
print('print()')
#f.write('write()');
#sys.stdout('sys.stdout()')
print('%f %#x'%(3.2,0x233))#顺序形式
#print('%(0)d'%(1,2,3))#这样不能用
print('%(a)d'%{'a':4,'b':5,'c':6})#字典形式 这里是直接使用的
print('format{}{}{}'.format(1,2,3))#顺序形式
print('format{2}{1}{0[1]}'.format((0,1),2,3))#索引形式
print('format{a:*^10}{b}{c}'.format(**{'a':6,'b':7,'c':8}))#字典形式
#str.rjust() str.ljust() str.conter() str.zfill()
print('**{!a} {!s} {!r}'.format('12\n','12\n','12\n'))#!a??
print('**',ascii('12\n'),str('12\n'),repr('12\n'))#ascii()??
print(repr('repr\n'))
print(eval('1+2+3'))

#f=open('path','r,w,a')
#f.read()
#f.readline()
#f.readlines()
#f.write()
#f.tell()#当前位置
#f.seek()#移动 ,0文件开头 ,1当前 ,2结尾往前
#f.close

print('*******pickle********')
import pickle
para_inf='para.inf'
arr=[]

def pickle_load(pa):
	f=open(pa,'ab+')
	f.seek(0,0)
	try:
		while 1:
			yield pickle.load(f)
	except EOFError:
		f.close()
		return


pi_it=pickle_load(para_inf)
#print(pickle.load(f))#EOFError
for i in pi_it:
	print(i,end=' ')
	if str(type(i)) == 'int':
		i=i+1
	arr.append(i)

#f=open(para_inf,'ab+')
#f.seek(0,0)
#for i in pickle.load(f):#居然不能迭代
#	print(i,end=' ')
#	if str(type(i)) == 'int':
#		i=i+1
#	arr.append(i)

if len(arr)==0:
	arr.append(1)
print('\n*******{}********'.format(arr))
arr[0]=(arr[0]+1)%10
i=1
while 1:
	j=input()
	if j=='':
		break;
	j=eval(j)
	if i<len(arr):
		if j==-1:
			arr.pop(i)
		else:
			arr[i]=j
			i=i+1
	else:
		arr.append(j)
		i=i+1
print('*******{}********'.format(arr))

f=open(para_inf,'wb')#重新创建防止数据重复
for i in arr:
	print(i,end=' ')
	pickle.dump(i,f)
f.close()

	