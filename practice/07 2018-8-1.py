#迭代器和生成器
#迭代器 访问集合元素
#可以记住遍历位置的对象 从第一个元素开始到所有元素分完结束 只前进
#iter() next()
li=[1,9,23,3]
it=iter(li)
print(next(it))
for i in it:
	print(i,end=' ')
print('')

#生成器 返回迭代器的函数

def li_iter(li_li):#生成器
	for li_i in li_li:
		yield li_i #每次next的返回值
	return#生成器结束


li=[5,5,4,4,123]
li_it=li_iter(li)#产生一个迭代器(但是type(li_it)的效果并不一样)
li_it1=li_iter('1234556')
it_li_it=iter(li_it)
print(type(it),'\n',\
	type(li_iter),type(li_iter(li)),type(li_it),type(iter(li_it)),'\n',\
	type(it_li_it),'\n',\
	type(next(li_iter(li))))
print(next(li_it))
li.append(100)
for i in li_it:
	print(i,end=' ')
print('')
for i in li_it1:
	print(i,end=' ')
print('')