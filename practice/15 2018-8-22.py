
import re
r=re.match('www', 'www.runoob.com')#起始位置匹配
print(r.group())#group对应正则表达式的每一个元素
print(r.start())#匹配的起始位置
print(r.end())#匹配的结束位置
print(r.span())#范围

 
###################################
#search任意位置匹配
line = "Cats are smarter than dogs";
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if searchObj:
	print ("searchObj.group() : ", searchObj.group())
	print ("searchObj.group(1) : ", searchObj.group(1))
	print ("searchObj.group(2) : ", searchObj.group(2))
#
line = "Cats are smarter than dogs";
 
matchObj = re.match( r'dogs', line, re.M|re.I)#起始位置匹配
if matchObj:
	print ("match --> matchObj.group() : ", matchObj.group())
else:
	print ("No match!!")
 
matchObj = re.search( r'dogs', line, re.M|re.I)#任意位置匹配
if matchObj:
	print ("search --> matchObj.group() : ", matchObj.group())
else:
	print ("No match!!")

phone = "2004-959-559 # 这是一个电话号码"
 
###################################
#替换
# 删除注释
num = re.sub(r'#.*$', "", phone)#替换
print ("电话号码 : ", num)
 
# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print ("电话号码 : ", num)

def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)
 
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))#用函数做替换的参数(用匹配字符串调用参数获取结果)

###################################
#compile 生成一个正则匹配方法
pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
print(m)
m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
print(m)
m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
print(m)                                         # 返回一个 Match 对象
m.group(0)   # 可省略 0
m.start(0)   # 可省略 0
m.end(0)     # 可省略 0
m.span(0)    # 可省略 0

###################################
#findall查找所有返回列表
pattern = re.compile(r'\d+')   # 查找数字
print('type(pattern):',type(pattern))
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)
 
print(result1)
print(result2)
print(re.findall(r'\d+','run88oob123google456'))
#re.和re.compile.差不多是可以混用的
###################################
#finditer查找所有返回迭代器
it = re.finditer(r"\d+","12a32bc43jf3") 
for match in it: 
    print (match.group() )