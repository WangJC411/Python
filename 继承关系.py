# -*- coding: UTF-8 -*-
#继承关系

'''
一个类可以把另一个类作为它的父类，这样就可以继承父类里面的参数

一个子类可以拥有多个父类，若父类之间有相同的方法名，则要涉及到访问顺序(广度优先)，查看顺序的代码为：
    import inspect
    print(inspect.getmro(cls))  或   print(cls.__mor__)    这边的cls要用子类名替换！！！
'''


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def information(self):
        print("{} is {} years ago.".format(self.name,self.age))
    def run(self):
        print('{} is runnning!'.format(self.name))
    def eat(self):
        print('{} is eating!'.format(self.name))


class Student(Person):
    def __init__(self,class1,name,age):
        self.class1=class1
        super(Student,self).__init__(name,age)   #调用父类__init__(可以省略第一个括号内的东西)
    def study(self,course):
        print('{} is studying {}.'.format(self.name,course))
    def run(self,distance):  #同名方法子类优先级大于父类
        print('{} runs {}km.'.format(self.name,distance))
    def eat(self,food):
        super(Student, self).eat()  #调用父类eat方法
        print('eat {}!'.format(food))

class Doctor(Person):
    def __init__(self,name,age,patients):
        super().__init__(name,age)
        self.patients = patients

list1=['A','B','C','D']
d = Doctor('boss_p',30,list1)  #把参数用列表的形式传递
s= Student('A',"Wang",21)
s.information()
s.run(100)
d.run()
s.study('Python')
s.eat('vegetable')
d.eat()


'''
输出结果：

Wang is 21 years ago.
Wang runs 100km.
boss_p is runnning!
Wang is studying Python.
Wang is eating!
eat vegetable!
boss_p is eating!

'''