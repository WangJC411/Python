# -*- coding: UTF-8 -*-
#系统高阶函数 (lambda function)
'''
lambda function (test = lambda x,y:x+y)可以分为三个部分：
第一部分：‘ = ’之前的为函数名(test)
第二部分：‘ lambda ’之后的为输入值(x,y)
第三部分：‘ ：‘之后的为满足条件的返回值(x+y)



'''
from functools import reduce

list1=[('Tom',19),('Tony',20),('Lily',18),('Jack',21),('Rose',23)]
#key = lambda x:x[1] 找出list1中，元组的第二个位置的值(在这边就是名字后面的数字),max函数是指找出最大值,min函数是找出最小值
max1=max(list1,key=lambda x:x[1])   #这个格式我想不明白，但是可以模仿着做
print('年龄的最大为',max1)
min1=min(list1,key=lambda x:x[1])
print('年龄最小为',min1)
s = sorted(list1,key = lambda x:x[1],reverse=True) #sorted 是把列表按照大小顺序进行排列，reverse=True表示从大到小，False表示从小到大
print('按照年龄排列后的顺序为：',s)
f=filter(lambda x:x[1]>20,list1)  #filter 是根据条件过滤，list1是在lambda函数后面的
print('年龄大于20的有：',list(f))  #要把f转成list形式，不然会是一个地址
m=map(lambda x:x[0].title(),list1)   #map是指映射，也就是提取list1中想要的值，进行操作之后放入一个新的list中。 title是指让字符串首字母大写
print('所有名字首字母大写：',list(m))
r=reduce(lambda x,y:x+y,[1,2,3,4,5,6,7,8,9])  #reduce是指对参数序列中的元素进行累积的动作(重复进行同一个动作)
print('1~9累加：',r)
#所有人年龄总和
t= reduce(lambda x,y:x+y,list(map(lambda x:x[1],list1)))  #先把所有人的年龄提取出来，然后做累加
print('所有人年龄总和为：',t)

'''
输出结果：

年龄的最大为 ('Rose', 23)
年龄最小为 ('Lily', 18)
按照年龄排列后的顺序为： [('Rose', 23), ('Jack', 21), ('Tony', 20), ('Tom', 19), ('Lily', 18)]
年龄大于20的有： [('Jack', 21), ('Rose', 23)]
所有名字首字母大写： ['Tom', 'Tony', 'Lily', 'Jack', 'Rose']
1~9累加： 45
所有人年龄总和为： 101

'''