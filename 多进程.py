# -*- coding: UTF-8 -*-
'''
多进程：
from multiprocessing import Process
process = Process(target = 函数 ，name = 进程的名字 ，args = 给函数传递的参数（元组的形式）)
process.start() 启动进程并执行任务
process.run() 不启动进程但执行任务
process.terminate() 终止进程
多进程对于全局变量访问，在每个全局变量里面都放一个m变量，保证每个进程的访问变量都互不干扰
'''

import time
import os
from multiprocessing import Process

list = []  # 不可变类型
m = 0  # 可变类型


def task1(s):
    while True:
        global m
        time.sleep(s)  # 睡眠时间通过调用函数时设定
        m += 1
        print("--->Task1", '--->', os.getpid(), '--->', os.getppid())  # os.getpid() 为当前进程id \ os.getppid() 为父进程id
        list.append(str(m))
        print('list1:', list)


def task2(s):
    while True:
        time.sleep(s)  # 睡眠时间通过调用函数时设定
        global m
        print("--->Task2", '--->', os.getpid(), '--->', os.getppid())
        m += 1
        list.append(str(m))
        print('list2:', list)


if __name__ == '__main__':
    print("当前进程的编号：", os.getpid()) #主进程当前的id
    print("父进程的编号：", os.getppid()) #主进程的父进程id
    p1 = Process(target=task1, name='任务1', args=(1,))  # args 要以元组的形式传递参数  此时args输入的是睡眠时间 1秒
    p1.start() #启动进程并执行任务
    print(p1.name)
    p2 = Process(target=task2, name='任务2', args=(2,)) # args 要以元组的形式传递参数  此时args输入的是睡眠时间 2秒
    p2.start() #启动进程并执行任务
    print(p2.name)

    num = 0
    while True:
        num += 1
        time.sleep(0.3)
        if num > 40: #当主进程运行40次时，结束 p1，p2
            p1.terminate() #结束进程
            p2.terminate() #结束进程
            break
        else:
            print(num)



'''
输出结果：

当前进程的编号： 2044
父进程的编号： 548
任务1
任务2
1
2
3
--->Task1 ---> 1020 ---> 2044
list1: ['1']
4
5
6
--->Task2 ---> 21628 ---> 2044
list2: ['1']
--->Task1 ---> 1020 ---> 2044
list1: ['1', '2']
7
8
9
--->Task1 ---> 1020 ---> 2044
list1: ['1', '2', '3']
10
11
12
13
--->Task2 ---> 21628 ---> 2044
list2: ['1', '2']
--->Task1 ---> 1020 ---> 2044
list1: ['1', '2', '3', '4']
14
15
16
--->Task1 ---> 1020 ---> 2044
list1: ['1', '2', '3', '4', '5']
17
18
19
--->Task2 ---> 21628 ---> 2044
list2: ['1', '2', '3']
--->Task1 ---> 1020 ---> 2044
list1: ['1', '2', '3', '4', '5', '6']
20
21
22
--->Task1 ---> 1020 ---> 2044
list1: ['1', '2', '3', '4', '5', '6', '7']
23
24
25
--->Task2 ---> 21628 ---> 2044
list2: ['1', '2', '3', '4']
26
--->Task1 ---> 1020 ---> 2044
list1: ['1', '2', '3', '4', '5', '6', '7', '8']
27
28
29
--->Task1 ---> 1020 ---> 2044
list1: ['1', '2', '3', '4', '5', '6', '7', '8', '9']
30
31
32
--->Task2 ---> 21628 ---> 2044
list2: ['1', '2', '3', '4', '5']
--->Task1 ---> 1020 ---> 2044
list1: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
33
34
35
--->Task1 ---> 1020 ---> 2044
list1: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
36
37
38
--->Task2 ---> 21628 ---> 2044
list2: ['1', '2', '3', '4', '5', '6']
39
--->Task1 ---> 1020 ---> 2044
list1: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
40

Process finished with exit code 0

'''