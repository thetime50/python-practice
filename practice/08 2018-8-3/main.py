def put_strlist(li):
	for i in li:
		print('\"'+i+'\"')
#
import sys
import mod
import mod2
#import pac1
from pac1 import *#__all__只对import *有效
from pac2 import *
from p3 import *
print('/////__name__:'+__name__+'//////\n')

print('\nsys.argv:')
put_strlist(sys.argv)
print('\nsys.path')
#put_strlist(sys.path)#这就是搜索包的路径

print(__name__)
put_strlist(dir())
print('//put_strlist(dir(sys)):')
#put_strlist(dir(sys))
#print(dir(mod))
#print(dir(pac))
