#在被外部模块引用时外部的代码作为初始代码
print('/////__name__:'+__name__+'///////\n')

def mod1_fun1():
	print('mod1_fun1')
#

#print(__file__+' init code too')

