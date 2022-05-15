# -*- coding: UTF-8 -*-
# 时间模块
import time
import datetime

a = time.time()#当前时间的时间戳
time.sleep(2)#睡眠2秒(暂停2秒)
b= time.ctime(a) #时间戳转字符串
c=time.localtime(a) #时间戳转元组
d=time.strftime('%Y-%m-%d  %H:%M:%S') #以想要的格式输出当前时间(字符串的形式)
e =time.strptime('2022/04/11','%Y/%m/%d') #以元组表示时间

print('当前时间的时间戳',a)
print('时间戳转字符串',b)
print('时间戳转元组',c)
print('以想要的格式输出当前时间(字符串的形式)',d)
print('以元组表示时间',e)
