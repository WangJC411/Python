# -*- coding: UTF-8 -*-
#关联关系

'''
类也可以做为对象传递，不同类之间会有关联关系

系统类型 : int,float,list,dicr...
自定义类型 : 各种自定义的类，例如这里的 Students,Computer,Book
'''

class Students:
    def __init__(self,name,computer,book):
        self.name = name
        self.computer=computer
        self.book=book
    def __str__(self):
        return self.name+'--'+str(self.computer)+'--'+str(self.book.booklist)  #self.name 是字符串对象，self.computer是自定义对象(类对象)，self.book.booklist是列表对象

class Computer:
    def __init__(self,brand,type):
        self.brand=brand
        self.type=type
    def __str__(self):
        return '品牌：{}，型号：{}'.format(self.brand,self.type)

class Book:
    def __init__(self,bname):
        self.bname=bname
        self.booklist=[]
        self.booklist.append(bname)
    def __str__(self):
        return '书名为',self.booklist

computer1= Computer('Apple',"Mac Pro")
book1=Book('完美世界')
print(type(book1.booklist))
student1=Students('Wang',computer1,book1)  #在Students类中用了其他类作为变数
print(student1)

'''
输出结果：

<class 'list'>
Wang--品牌：Apple，型号：Mac Pro--['完美世界']

'''