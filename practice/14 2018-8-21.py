#python 标准库
####
def put_list(li):
	print('\n')
	for i in li:
		print('\''+str(i)+'\'')

import os
print('>>>',os.getcwd())
#if input()=='c':
#	a=os.system('cls')
#put_list(dir(os))
help(os.getcwd)

#当前目录文件搜索
import glob
print(glob.glob('*.py'))
#help(glob)

#命令行参数
import sys
put_list(sys.argv)

#出错终止
#sys.stderr.write('error info')

#正则
import re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(type(r'str'),r'str\n')
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))

#math

#net

#date
from datetime import date
now=date.today()
print(now)
#print(dir(now))
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
print(type(now),type(now.ctime()),'  ',now.ctime())
class Cl_date(date):
	def get_mro(self):
		return self.__class__.mro()
print(Cl_date(2018,6,21).get_mro())
birthday = date(1994, 5, 1)
print(now-birthday)

#压缩
import zlib,gzip,bz2,zipfile,tarfile
da=b'hello world!'
for i in range(4):#(10):
	print(len(da),da)
	zda=zlib.compress(da)
	print(len(zda),zda)
	zda=gzip.compress(da)
	print(len(zda),zda)
	zda=bz2.compress(da)
	print(len(zda),zda)
#	zda=zipfile.compress(da)
#	print(len(zda),zda)
#	zda=tarfile.compress(da)
#	print(len(zda),zda)
	print('')
	da=da+b' world!'

#性能度量
from timeit import Timer
import timeit
s=str(da)
print(s)
print(Timer('zlib.compress(da)','import zlib;da='+s).timeit(number=1000))
print(Timer('gzip.compress(da)','import gzip;da='+s).timeit(number=1000))
print(Timer('bz2.compress(da)','import bz2;da='+s).timeit(number=1000))
#https://www.cnblogs.com/itcomputer/articles/4578769.html
#https://www.cnblogs.com/piperck/p/6287903.html
print(dir(timeit))
print(dir(Timer))
#timeit.timeit=timeit.Timer.timeit
#code_str="""
#"""
#Timer(Timer,...)

#:mod:profile 和 pstats ??

def average(values):
	'''
	>>> print(average([20, 30, 70]))
	40.0
	'''
#	'''
#	>>> print(average([20, 30, 80]))
#	40.0
#	'''
	return sum(values) / len(values)

import doctest
doctest.testmod()#将函数里第一段字符串注释复制到解释器中执行,正常无反应

#unittest
import unittest
class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)
#

def add(a, b):
    return a+b

def minus(a, b):
    return a-b

def multi(a, b):
    return a*b

def divide(a, b):
    return a/b
#

class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    def test_add(self):
        """Test method add(a, b)"""
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        """Test method minus(a, b)"""
        self.assertEqual(1, minus(3, 2))

    def test_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(6, multi(2, 3))

    def test_divide(self):
        """Test method divide(a, b)"""
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))


if __name__ == '__main__':
	unittest.main() # Calling from the command line invokes all tests
#https://www.cnblogs.com/fennudexiaoniao/p/7771931.html
#http://blog.csdn.net/huilan_same/article/details/52944782
