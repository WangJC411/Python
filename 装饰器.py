# -*- coding: UTF-8 -*-
# 装饰器 decorator

'''
装饰器的作用就是在不改变原程式的情况下加入一些东西到原程式里

装饰器格式：
def decorator(func):
    def inner(参数...):
        ...
    return
@decorator  #相当于： 原函数 = decorator(原函数)
def 原函数():
    ...
'''


def decorator(func):
    def inner(*args, **kwargs):  # *args表示拆包元组，**kwargs表示输入参数时用关键字形式
        func(*args, **kwargs)
        print('一层')
        print('二层')
        print('三层')
        print('顶层')

    return inner
# 加了*args和**kwargs后，不同函数调用装饰器都可以不限制类型，如：NB有四个输入值，SH只有三个，但是装饰器都可以接收

@decorator
def NB(address, owner, value, area):
    print('房子的地址为{}，拥有者为{}，占地面积为{}平，价值{}'.format(address, owner, area, value))


@decorator
def SH(address, value, area):
    print('{}的房价为{}万/平，面积为{}平'.format(address, value, area))


@decorator
def JD(name, address, area):
    print('酒店的名称为{}，地址是{}，面积为{}平'.format(name, address, area))


NB('宁波', 'Wang', 200, '一千万')
SH('上海', 3, 100)
JD('沙县大酒店', '鄞州区', 40)

'''
输出结果：
房子的地址为宁波，拥有者为Wang，占地面积为一千万平，价值200
一层
二层
三层
顶层
上海的房价为3万/平，面积为100平
一层
二层
三层
顶层
酒店的名称为沙县大酒店，地址是鄞州区，面积为40平
一层
二层
三层
顶层
'''
