# -*- coding: UTF-8 -*-
'''
面向对象：
面向对象一共有4种东西组成----类、对象、属性、方法
类-----手机类
对象-----某某某的手机...
属性-----手机的品牌，内存大小，颜色...
方法-----打电话，发短信，上网

'''


# 普通方法
import sys


class Phone:  # 类的首字母一定要大写
    brand = 'Apple'  # 类属性
    price = 7999  # 类属性
    type = 'iphone 13pro'  # 类属性

    def call(self):  # 方法
        print('-----正在打电话-----')
        print('留言：', self.note)


phone1 = Phone()
phone1.note = 'phone1的留言'  # 新建一个对象属性
print(phone1)  # phone1的地址
print(phone1.price)  # 打印对象属性
phone1.call()  # 调用方法时会自动把自身的地址上传
phone2 = Phone()
phone2.note = 'phone2的留言'
phone2.call()
phone2.brand = 'Huawei'  # 把类属性拿下来后，赋予新值作为对象属性(不会影响类属性)
print(phone1.brand, phone2.brand)

'''
输出结果：

<__main__.Phone object at 0x00000195E8A1FFD0>
7999
-----正在打电话-----
留言： phone1的留言
-----正在打电话-----
留言： phone2的留言
Apple Huawei

'''

# 类方法
'''
1、定义需要依赖装饰器@classmethod，不依赖对象
2、类方法中参数不是一个对象，而是类或者类属性
3、类方法中只可以使用类属性，不能使用对象属性
4、类方法中不能调用普通方法

类方法的作用：在对象创建之前(此时还没有对象)，需要完成一些动作，可以用类方法
'''


class Dog:
    def __init__(self, nickname):
        self.nickname = nickname

    @classmethod  # 类方法
    def test(cls):  # cls与普通方法中的self性质相似
        print('------test------')


Dog.test()  # 不需要对象，直接调用
# 输出结果 ： ------test------

# 静态方法
'''
1、需要装饰器@staticmethod
2、无需传递参数(self，cls)
3、只能访问类属性和类方法，无法访问对象
4、加载时机同类方法
'''


class Person1:
    @staticmethod  # 静态方法
    def test():
        print('---静态方法---')

    age = 18

    @staticmethod
    def age1():
        print('年龄：', Person1.age)


Person1.test()  # 调用静态方法
Person1.age1()  # 调用静态方法


# 魔术方法
# __init__方法
class Phone1:
    def __init__(self):
        print('----__init__----')
        self.brand = 'xiaomi'
        self.price = 4999


phone1 = Phone1()  # 此时phone1对象中已经有对象属性brand和price
# 因为Phone1里面有__init__方法，在调用Phone1时会进入init方法执行里面的动作，然后再讲内存地址给phone1

'''
输出结果：----__init__----
'''


# __new__方法
class Person2:
    def __init__(self):
        print('---__init__---')

    def __new__(cls):
        print('---__new__---')
        ret = super().__new__(cls)  # 对象的地址
        print(ret)
        return ret


p = Person2()  # 在加载Person2的时候已经触发了__new__方法，触发时机比__init__还要之前
print('-----------------------------')
print(p)
# __new__与__init__不同点是，__new__ 負責物件的建立而 __init__ 負責物件的初始化
'''
输出结果：

---__new__---
<__main__.Person2 object at 0x00000294794CFB50>
---__init__---
-----------------------------
<__main__.Person2 object at 0x00000294794CFB50>

'''


# __call__方法
class Number:
    def __call__(self, num1, num2):
        add = num1 + num2
        return add


t = Number()
print(t(3, 8))  # 将对象当成函数用时，会默认调用__call__里的内容
# 输出结果： 11
# 如果正常写的话，应该先写一个add的普通方法(输入两个值，然后返回相加值),然后再调用这个函数，打印返回值
# 要是用__call__方法程式就会比较简单


#__str__方法
class Person5:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name


p=Person5('Jack')
print(p)  #原本p打印出来应该是它的地址，但是因为有__str__函数，所以把原本的地址变成了return值
#输出结果： Jack


#__del__方法
'''
当引用对象都手动删完之后或者本次执行结束后(python解释器会回收所有在本次执行过程中的空间，也就是自动删除所有引用对象)，执行__del__的内容
'''

class Person4:
    def __init__(self):
        pass
    def __del__(self):
        print('---已删除---')

p1=Person4()
p2=p1
p3=p2
p4=p1
#p1,p2,p3,p4都指向同一个地址
del p2
del p3
print(sys.getrefcount(p1))  #打印对p1引用的次数(这行代码本身也是对p1的引用，所以次数会+1)
'''
输出结果：
3
---已删除---  #这里的删除是因为执行结束,所以一直会在最后一行出现
'''

