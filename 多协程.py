# -*- coding: UTF-8 -*-
# 多协程
'''
协程可以理解为微线程，相当于线程与进程之间的关系
多协程工作时，当一个协程进行耗时操作时，就会切换到另一个协程上，并在适当的时机切换回来

下载greenlet来手动切换不同任务

下载gevent来实现自动切换，gevent底层还是使用greenlet，只是封装了自动切换的功能
实现自动切换功能的是里面的猴子补丁
猴子补丁是把系统的time.sleep()改成了gevent.sleep(),然后gevent能够捕捉到gevent.sleep()
并且在之前进行切换协程的动作

注：有一点很奇怪，在用greenlet的时候时间跟用生成器时是一致的，但是在用gevent的猴子补丁时，时间明显变短，而且结果出来的顺序不一样
感觉sleep()的时间明显有被跳过，真正有做到省时
'''
import time

# 通过生成器的方式进行操作(只是进行了交叉运算，并没有在进行耗时操作时进行切换)
from greenlet import greenlet


def task1():
    for i in range(5):
        print('A', i)
        yield
        time.sleep(0.2)


def task2():
    for i in range(5):
        print('B', i)
        yield
        time.sleep(0.2)


g1 = task1()
g2 = task2()

while True:
    try:
        next(g1)
        next(g2)
    except:
        break
'''
输出结果：

A 0
B 0
A 1
B 1
A 2
B 2
A 3
B 3
A 4
B 4

'''

# 利用greenlet模块进行手动切换
start = time.time()


def a():
    for i in range(5):
        print('AAA', i)
        gb.switch()  # 在sleep之前切换到协程b上
        time.sleep(0.8)


def b():
    for i in range(5):
        print('BBB', i)
        gc.switch()  # 在sleep之前切换到协程c上
        time.sleep(0.4)


def c():
    for i in range(5):
        print('CCC', i)
        ga.switch()  # 在sleep之前切换到协程a上
        time.sleep(0.2)


ga = greenlet(a)
gb = greenlet(b)
gc = greenlet(c)
ga.switch()  # 切换到协程a上

end = time.time()
print(end - start)  # 计算耗时

'''
输出结果：

AAA 0
BBB 0
CCC 0
AAA 1
BBB 1
CCC 1
AAA 2
BBB 2
CCC 2
AAA 3
BBB 3
CCC 3
AAA 4
BBB 4
CCC 4
6.481142282485962

'''

# 使用gevent进行协程之间的自动切换
import gevent
from gevent import monkey

monkey.patch_all()  # 猴子补丁，实现自动切换

start = time.time()
def aa():
    for i in range(5):
        print('AAA', i)
        time.sleep(0.8)


def bb():
    for i in range(5):
        print('BBB', i)
        time.sleep(0.4)


def cc():
    for i in range(5):
        print('CCC', i)
        time.sleep(0.2)


if __name__ == '__main__':
    gg1 = gevent.spawn(aa)
    gg2 = gevent.spawn(bb)
    gg3 = gevent.spawn(cc)

    gg1.join()
    gg2.join()
    gg3.join()

end = time.time()
print(end - start)  # 计算耗时

'''
输出结果：

AAA 0
BBB 0
CCC 0
CCC 1
BBB 1
CCC 2
CCC 3
AAA 1
BBB 2
CCC 4
BBB 3
AAA 2
BBB 4
AAA 3
AAA 4
4.026420593261719


'''