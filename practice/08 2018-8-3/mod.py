#在被外部模块引用时外部的代码作为初始代码
import mod1
print('/////__name__:'+__name__+'///////\n')

def mod_fun1():
	print('mod_fun1')
#

print(__file__+' init code too')

