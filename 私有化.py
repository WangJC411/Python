# -*- coding: UTF-8 -*-
# 私有化
# 公有：在类之外可以更改，可以单独访问
# 私有：在类之外不可以更改，不可以单独访问

# 第一种写法：
# 用两个不同的普通方法来分别设置获取私有变量和给私有变量赋值
class Students:
    def __init__(self, name, age):
        self.name = name  # 公有：在类之外可以更改，可以单独访问
        self.__age = age  # 私有：在类之外不可以更改，不可以单独访问

    def __str__(self):
        return '姓名：{}，年龄：{}'.format(self.name, self.__age)

    def getAge(self):  # 通过一个普通方法访问私有变量
        return self.__age

    def setAge(self, age):  # 通过一个普通方法给私有方法赋值
        if age > 0:  # 可以对赋值进行限制
            self.__age = age
        else:
            print('error!')


x = Students('abc', 12)  # 输入姓名和年龄，年龄是私有变量
print(x)  # 姓名：abc，年龄：12
x.setAge(21)  # 通过之前的方法更改私有变量
print(x)  # 姓名：abc，年龄：21
print(x.getAge())  # 21

'''
输出结果：

姓名：abc，年龄：12
姓名：abc，年龄：21
21

'''


# 第二种写法：
# 用一种方法加上两个不同的装饰器来对私有变量获取和赋值
class Students1:
    def __init__(self, name, age):
        self.name = name  # 公有：在类之外可以更改，可以单独访问
        self.__age = age  # 私有：在类之外不可以更改，不可以单独访问

    def __str__(self):
        return '姓名：{}，年龄：{}'.format(self.name, self.__age)

#需要先写get的部分，再写set的部分
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0:  # 可以对赋值进行限制
            self.__age = age
        else:
            print('error!')


x = Students1('xyz', 20)  # 输入姓名和年龄，年龄是私有变量
print(x)  # 姓名：xyz，年龄：20
x.age = 21  # 对私有变量重新赋值
print(x)  # 姓名：xyz，年龄：21
print(x.age)  # 获取私有变量，不需要加() 21

'''
输出结果：

姓名：xyz，年龄：20
姓名：xyz，年龄：21
21

'''
