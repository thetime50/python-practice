#字典
dic={'key':'value',1:2,(3,4):5}
print(dic,dic['key'],dic[1],dic[(3,4)])
#key必须是唯一的 不可变类型
dic['new']='n'#用等式添加新的成员 与其特类型不同
print(dic)

del dic['new']#和列表类似
print(dic)
dic.clear()#清空
print(dic)
del dic#删除

#初始化时相同的键后面的有效

#字典函数
print('\n字典函数')
dic={'key':'value',1:2,(3,4):5}
print(len(dic),str(dic),type(dic))

#字典方法
print('\n字典方法')
#dic.clear()#删除
dic1=dic.copy()
print(dic1)
dic1=dic.fromkeys(('a','b','c'))#按元组和初始值创建新字典 默认值为none
dic2=dic.fromkeys((1,2,3),4)
dic3=dic.fromkeys((4,5,6),(7,8,9))#元组只当做一个元素
print('\n',dic,'\n',dic1,'\n',dic2,'\n',dic3)
print(dic.get('err','error str'))#安全的key索引
print(dic.setdefault('key'),'\n',dic.setdefault('new','n'),'\n',dic)#初始化 若已存在则返回当前值
print('key' in dic,'value' in dic)#字典的 in 运算是对应key的
print(dic.items())#返回[(key,value),...]的元组数组
print(dic.keys(),dic.values())
dic.update({'new':1,'new1':2})#添加或覆盖字典
print(dic)
print(dic.pop('none','no find key'),'\n',dic.pop('new1'),'\n',dic)#查找推出
print(dic.popitem(),'--',dic)#推出

#####################################################
####集合#############################################
#和字典一样 集合内必须是常量
s=set()#空集合
print('type({}):',type({}),'type(set()):',type(set()))
#in
#- | & ^#位运算符和一个减号
s={1,2}
s.add(3)#添加项目
print(s)
#s.update(({4,5[6,(7,8)]},{9:10}))
s.update([(1,2),3],[6])#添加列表 有点迷 会解开 可以是多个列表
print(s)
#li=[1,2,3],[4,5,6]
#print(li)
s.remove(3)
print(s)
s.discard(2)#不报错
print(s)
print(s.pop(),s)
print(len(s))
s.clear()
print(s)

