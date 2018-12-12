from pac.pacm1 import *

class clas:
	a=3
	print('clas',a)
	#__b#私有属性
	def __init__(self,i):#第一个参数默认是实例指针
		print('clas init')#实例初始化时运行
		self.i=i
		self.a=self.a+i
	print('clas end')#class 声明时运行
c=clas(3)
print(c.i,c.a)
cc=clas(1)
print(cc.i,cc.a)

c1=clas1(1,2)
print(c1.v1,c1.v2)
c1.put_dir()

print('\n\n继承\n')
import pac.pacm2
print('************',dir(pac))
class jc_clas(clas,pac.pacm2.clas2):#好像只能继承class不能是model 或者 packeg
	def __init__(self):
		print('jc_clas init')
		print(dir(self))
		print(dir())
		#__init__方法被重写了
		clas.__init__(self,1)
		pac.pacm2.clas2.__init__(self,2,3)
		#clas1.__init__(pac.pacm1.self,2,3)#这样也可以??
	def fun(self):
		print('jc_clas fun()')
	def clas1_fun(self):
		super().fun()
#
jc=jc_clas()
jc.fun()
super(jc_clas,jc).fun()
jc.clas1_fun()

print('\n\n\n类属性与方法\n')
#私有属性和私有方法以__开头 只能在class内使用

print('\n\n\n专有方法和运算符重载\n')
class Cl_a:
	print('Cl_a')
	def __init__(self,a):
		print('Cl_a init')
		self.a=a
	def __del__(self):
		print('Cl_a del')

class Cl_b:
	print('Cl_b')
	def __init__(self,b):
		print('Cl_b init')
		self.b=b
	def __del__(self):
		print('Cl_b del')

class Cl_xa(Cl_a,Cl_b):
	print('Cl_xa')
	def __init__(self,xa):
		Cl_a.__init__(self,xa)
		Cl_b.__init__(self,xa)
		print('Cl_xa init')
		self.xa=xa
	def __del__(self):
		Cl_a.__del__(self)
		Cl_b.__del__(self)
		print('Cl_xa del')

xa=Cl_xa(1)
del xa

class Cl_p:
	def __init__(self,v):
		self.v=v
	def __add__(self,t):
		print('Cl_p',self,t)
		return self.v+t.v
class Cl_pp(Cl_p):
	def __add__(self,t):
		print('Cl_pp',self,t)
		return self.v+t.v+1
class Cl_ppp():
	def __init__(self,v):
		self.v=v
	def __add__(self,t):
		print('Cl_ppp',self,t)
		return self.v+t.v+2

p=Cl_p(1)
pp=Cl_pp(2)
ppp=Cl_ppp(3)
print(p.v,pp.v)
print(p+p,pp+pp,p+pp,pp+p)#使用用前面实例的方法
#print(p+pp+ppp)#报错了,__add__不能处理int类型
print(ppp+p)#不论是否是同类或者继承关系都可以运算

class Cl_cp:
	def __init__(self,a):
		print('Cl_cp init',a)
		self.a=a
	def __add__(self,t):
		m=Cl_cp(self.a)
		m.a=m.a+t.a
		return m
	def __del__(self):
		print('Cl_cp del',self.a)
#	def __repr__(self):
#		return str(self.a)
cp=Cl_cp(3)

print(cp+cp+cp+cp)
print(str(cp))