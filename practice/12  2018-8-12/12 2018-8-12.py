import sys
import os

def put_arr(a):
#	print(type(a))
#	print(a)
	for i in a:
#		print(type(i))
		print('\''+str(i)+'\'')
	print('')

def tfun(i):
	print(100/(i-10))

while True:
	try:
		x=int(input('please input number:'))
		print(100/x)
		tfun(x)#函数里发生的异常会被抛出
		#break#break会直接跳出循环不执行else
	except ValueError:#捕获并清除错误 (因为是意料之内
		print('retry')
	except (RuntimeError, TypeError, NameError):#可以在元组里
		print('error tuple')
		print('retry')
	except:
		print('其他错误')
		put_arr(sys.exc_info())#错误信息类型 说明 
		print('retry')
	else:
		print('hello')
		print('正常执行\n')
		break
#
#while True:
try:
	f=open('myfile.txt')
	s=f.readline()
	i=int(s.strip())
except OSError as err:
	print('\''+str(err)+'\'')#只有说明信息
	put_arr(sys.exc_info())
#

#raise err

def raise_fun():
	try:
		a=1/0
	except:
		print('捕获到异常 raise重新抛出')
		put_arr(sys.exc_info())
		raise

try:
	raise_fun()
except:
	print('捕获到raise_fun()异常')
	put_arr(sys.exc_info())
#
def finally_fun():
	try:
		a=1/0
#	finally ZeroDivisionError:#是不能用的
#		print('finally捕捉到ZeroDivisionError异常但不清除')
#		put_arr(sys.exc_info())
	finally:#不论是否有异常总是执行 也不会清除异常
		print('finally不清除')
		put_arr(sys.exc_info())

try:
	finally_fun()
except:
	print('捕获到finally_fun()异常')
	put_arr(sys.exc_info())
#

try:
	raise TypeError#抛出指定异常
except:
	put_arr(sys.exc_info())

#自定义异常
class AbcError(Exception):
	#def __init__(self,value):
	#	self.value=value
	def __str__(self):#需要含有这个对象
		return 'this is AbcError'#repr(self.value)

try:
	#raise AbcError(2)
	raise AbcError
except AbcError:
	put_arr(sys.exc_info())





#or line in open("myfile.txt"):
#    print(line, end="")
#这里文件不会被关闭
#with open("myfile.txt") as f:
#    for line in f:
#        print(line, end="")
#这里会关闭文件

a=input('exit')
if a=='':
	a=os.system('cls')

