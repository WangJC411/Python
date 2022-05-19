# -*- coding: UTF-8 -*-
# 循环导入
# 循环导入是错误架构
#把导入的语句放入函数中，可避免循环导入

'''
例如：(当做训练逻辑，正常程式不会套来套去，循环1和循环2是两个py程式)
循环1模块：
from 循环2 import func
def task1():
    print('__task1__')
def task2():
    print('__task2__')
    func()
task1()
task2()

循环2模块：
def func():
    print('func----1')
    from 循环1 import task1
    task1()
    print('func---2')

'''
'''
输出结果：
注：在循环2func()中，若已导入过一次循环1，第二次遇到就会跳过这个步骤
1    __task1__   #循环1本身执行task1
2    __task2__   #从这行开始，循环1本身执行task2，到第10行结束
3    func----1   
4    __task1__
5    __task2__   #从这行开始，循环2中加载循环1中的task2，到第8行结束
6    func----1   
7    __task1__   
8    func---2    
9    __task1__
10    func---2

Process finished with exit code 0


'''