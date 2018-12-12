#列表
li=[1,2,'123',4,5]
print(li)
print(li[0],li[-5],li[2:-1],li[3:2])
#li[:-]
#del li[1]
del li[1]
print(li,li[1])

#len()
#[]+[]
#*
#in
#for x in []

#列表函数
print('\n\n列表函数')
li=[5,6,65,6,67,2334]
print(len(li),max(li),min(li),list((3,4,5)))

#列表方法
print('\n\n列表方法')
print(li)
li.append(3)#在末尾添加
print(li)
li.extend((4,3,2))#末尾添加列表
print(li)
li.insert(3,2333)#插入
print(li)
li.pop(1)#default -1#移除并返回元素
print(li)
li.remove(6)#搜索移除
print(li)
li.reverse()#倒序
print(li)
li.sort()#排序
print(li)
li1=li
li2=li.copy()
li1[1]='li1'
li2[1]='li2'
print(li,li1,li2)
print(li.count(5))#计数
print(li.index(5))#查找
li.clear()
print(li)

#元组
print('''
////////////////////////////
//元组//////////////////////''')
#len()
#+
#*
#in
#for x in ()
print(tuple([1,2,3]))


