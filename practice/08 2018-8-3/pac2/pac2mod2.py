#import pac2mod1#这样是不行的
#import .pac2mod1#这样是不行的
#from pac2mod1 import *#这样是不行的 搜索路径不会不含当前文件夹
from .pac2mod1 import *
#from ..pac1.pac2mod1 import *#报错 尝试相对导入超出顶级包
import sys
def put_strlist(li):
	for i in li:
		print('\"'+i+'\"')

print('__name__:'+__name__)
print('__package__:'+__package__)
put_strlist(sys.path)#这里不会包含包里面的路径 只有项目根文件夹