#默认UTF-8编码
'''使用 # -*- coding: cp-1252 -*- 指定编码格式'''
print('hello')

#注释
"""注释"""
'''注释'''

a=1+2+3\
	+4+5+6
b={1,2,3,#{} [] () 内不用\
	4,5,6}
print(a,b)

int_v=123
bool_v=True
floult_v=1.2E-3
complex_v=1.2E-3+1.2E-3j

print(int_v, bool_v, floult_v, complex_v)

str='123'#"123"
strm="""
123
456
"""
str1=r"123\n456"#不转义\
str2='123\n''456'#转义 拼接 同c
#str[1]=2 #error 不能改
#没有字符类型啊没有字符类型
print('\n\n*str note')
print(str,strm,str1,str2)
print(str[0:-1]*2+str1)
'''
i=input("提示")
print(i)

i=input("提示");print(i)#像c 同一行多条语句用;分隔
'''
print("替换结尾", end="");print("next print")

#import module #module.fun
#from module import fun1,fun2 #fun1 fun2
#form module input * #import all #fun1 ...

import sys
for i in sys.argv:
	print(i)

#$python -h

#基本数据类型
#Number 数字
#String 字符串'' "" """ ''' r' ''[0:-1] + * 
#List	列表[] arr [0:-1] + * 
#Tuple	元组(,) const arr type((2))是int
#Set	集合{} - & | ^ in 空集合set()
#Dictiona 字典{:}空字典{}  dict()
class A:
	pass
class B(A):
	pass
print(type(sys))
print(type(A())==A)
print(isinstance(A(),A))
print(type(B())==A)#更严格
print(isinstance(B(),A))#实例 

del A,B#删除多个对象 类似定义

#运算 以下按优先级排
#+ - * / % //整除 **乘方
#== != > < >= <=
#<< >> & | ^ ~ 
#is  not is身份运算符 是不是来自相同对象的引用id(x)==id(y)
#in  not in成员
#and or not
print('\\')#\ 转义
repr('\\')#\\\\ 反转义
eval('print(str)')#字符串中有效表达式转换为表达式 str to code
print(frozenset([1,2,3]))#不可变集合??
print(chr(48)+'1')#int to char(str)
print(ord('0'))#char to int
print(hex(170))#int to hex_str
print(oct(8))#int to oct_str

i=int(2.3)
f=float(1)
c=complex(2)
c1=complex(2,3)
print(i,f,c,c1)
print(7/2,7.0/2,7/2.0)#类型提升
5+2
#print(_) 交互模式下 最后的运算结果赋值给_

from math import *
print('\r\nmeth fun')
print(ceil(1.1),floor(2.9))
print(abs(-1),abs(-1.0),fabs(-1),fabs(-1.0))
print(max(1,2,3,4,5,32,6))#min
print(modf(1.2))#分离整数 小数 返回元组
print(round(1.4),round(1.5),round(-1.4),round(-1.5),round(23.4,-1))#四舍五入

#随机数
from random import *
print('\nrandom\n')
print(choice(['123',4,5,(6,7,8)]))#随机选出序列中的元素
print(randrange(-20,4,2))#在等差数列中选取随机数
print(random())#随机0>random()>1
seed(2)#seed([])初始化种子
li=[1,2,3,4,5]
shuffle(li)
print(li)#随机排列序列
print(uniform(-20,4))#随机数
print('e',e,'pi',pi)