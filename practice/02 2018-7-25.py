#字符串
#py中并没有单个的字符

print('abcdefghij'[-10:9],'abcdefghij'[0:1])
print('ab'+'bcd'[1])
print('\'\\060\'','\060')#八进制 同c
print('\'\\x30\'','\x30')#16进制 同c

#字符运算符
#+ * [] [:]
#in  not in
#r R 原始字符串 不转义但是%是用%%表示的
#% 格式化字符
str=r'''123
123\n123'''
print(str)#并不是反转义 而是原样输出
str='''123
123\n123'''
print(str)
print('%% %%d %d'%(3))
print('%%%% %% %%s %s %%d %d'%('123',3))
print('%%c %c'%('x'))#多余的字符会报错
print('%#x'%(-0x30))#菜鸟说是无符号的，但是有符号的可以显示
'''
%c %s %d %u
%o %x %X %#x
%f %e %E %g %G
%p 指针用
'''
print('%(tag1)d %(tag2)s'%{'tag2':'tag2 666','tag1':123})
print('%(f)-05.2f'%{'f':7.6})#好像有些标识没什么用 大体同c

#str.format()
#'{[]}'用{}标识
print('\n\nstr.formate')
print('{}{}'.format(12,'34'))
print('{1}{0}{1}'.format(12,'34'))#用下标表示
a=10
print('{a}{b}'.format(b='bstr',a='astr'))#用等式表示
print(a)

site={'b':'bstr','a':'astr'}
print('{a}{b}'.format(**site))#用字典表示 不明
print('{a}{b}'.format(**{'b':'bstr','a':'astr'}))#用字典表示
print('123 {0[1]} {1[0]}'.format([1,23],[4,56]))#在格式字符串内进行成员操作.等
print('{0:5.3f}'.format(12,'34'))#用下标表示 :格式化
print('{:0^10}'.format(12))#居中
print('{:0>10}'.format(12))#右对齐
print('{:0<10}'.format(12))#左对齐
print('{0:#b} {0:#o} {0:#d} {0:#x}'.format(40))
print('}} {{ \\ %% \' %d'%(1))#用format 会转义 }} {{ 用%会转义%%
print('{:,}'.format(123456.654321))#数字用,分割
print('{:.2%}'.format(1.02))
#相比%()节省了名字用序号代替 可以忽略类型

#string 方法
print('\nstring方法\n')
str='hello'
print(str.capitalize(),str)#首字母大写 不会改变原字符串
print(str.center(2,'-'),str.center(10,'-'))#扩充并填充居中字符串
print('hello'.ljust(10,'-'))#扩充并填充左对齐字符串
print('hello'.rjust(10,'-'))#扩充并填充右对齐字符串
print('hello'.zfill(10))#扩充右对齐填'0'
print(str,str.count('l',0,-1))#统计字符串
print('你好'.encode('UTF-8'),'你好'.encode('utf-8'),'你好'.encode('GBK'))
print('你好'.encode('UTF-8').decode('UTF-8'))#python 3 str没有decode方法 但是encode后有
print(type('你好'),type('你好'.encode('UTF-8')),\
	type('你好'.encode('UTF-8').decode('UTF-8')))
print(str.startswith('he'),str.startswith('e'))#起始字符串检查
print(str.endswith('lo'),str.endswith('l'))#结束字符串检查
print('123	4567	89	0'.expandtabs(4))#table替换为指定数量的空格
str='12345678956'
print('finrd',str.find('56'),str.find('01'))#字符串查找
print('rfind',str.rfind('56'))#从右查找
#print(str.index('56'),str.index('01'))#字符串查找 没找到会报异常
print('123jadf'.isalnum(),'213.m'.isalnum())#只有字母数字
print('asdf'.isalpha(),'2asd'.isalpha())#只有字母
print('452423'.isdigit(),'3242s'.isdigit())#只有数字
print('34a'.islower(),'23A'.islower(),'23'.islower())#有字母且只有小写
print('AS33'.isupper(),'Ad234'.isupper())#有字母 且只有大写
print('123'.isnumeric(),'13a'.isnumeric())#只有数字 罗马 汉字
print(' 	 	\n'.isspace(),'sd 	'.isspace())#只有空白字符
print('abc def'.title(),'abc def'.title().istitle(),'bac def'.istitle())#标题格式 是标题格式
print(len('sadfas'))#字符串长度
print('ASD'.lower(),'asd'.upper())#大小写转换
print('dafDAasdf'.swapcase())#大小写互换
print('  sd  '.strip())#去掉两侧字符
print('  	123'.lstrip(),'121232'.lstrip('12'))#去掉左侧字符
print('123  	'.rstrip(),'3212a12'.rstrip('12a'))#去掉右侧字符
print('87654321'.translate(str.maketrans('123456','abcdef')))#创建转换表 转换字符串
print(max('12ads,'),min('12ads,'))#最大最小
print('asdasdasdasd'.replace('da',':ad:',2))#替换字符串
print('asdfasdfasdf'.split('df',2))#分隔字符串
print(':a:'.join(['123','345','23']))#以本字符串连分隔列元素
print('asde\rasd\n'.splitlines())#分隔行
print('31234'.isdecimal(),'12qw'.isdecimal())#只有数字unicode

print(b'asd')
