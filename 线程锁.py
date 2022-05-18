# -*- coding: UTF-8 -*-
# 线程锁
'''
GIL  全局解释器锁
    python底层会默认给线程加GIL
    存在这个的原因是原本线程存在数据不安全的情况，例如：
    在执行n+=1时，对于程式而言，会有两步：
                            第一步：n+1
                            第二步：n=n+1
    因为多线程在执行时是频繁在切换的，有可能会出现在一个线程执行第一步时，就被切换到其他线程的情况
    这样这个全局变量虽然进行了+1的动作，但是没有赋值给n，所以数据就会与预想的不一致，也就是数据不安全
    为了避免这个问题，python就在线程中默认设置了‘线程同步’(加锁)这个规则
    这个规则就是让一个线程不完整操作完就不会被砍掉，但是线程同步这个规则会使多线程的效率降低
    如果是数字只有4.5位就不会有太多问题，但是数字很大时，就会有影响
    所以，为了不影响运算效率，当线程中遇到数字很大的情况，这个锁就会被释放
    锁被释放的时机是与运算率上限有关。数字大，运算率就大，突破上限后，GIL就会被释放，但是会出现数据不安全的情况

如果要优先考虑数据的安全性，就要在数字大的时候手动加锁
lock = threading.Lock
lock.acquire()  #获取线程锁  (如果锁已经被其他线程拿去使用，则需要等待锁的释放)
...   线程具体的操作要被夹在这两条代码之间
lock.release()   #释放线程锁


死锁：
开发过程中使用线程，在线程之间共享多个资源的时候，如果两个线程分别占有一部分资源并且同事等待对方的资源，就会造成死锁。
尽管死锁很少发生，但是一旦发生就会造成应用的停止响应，程式不做任何事情

【线程A】--->(需要X线程锁，才释放Y线程锁)--->【进程】
【线程B】--->(需要Y线程锁，才释放X线程锁)--->【进程】
这时两个线程之间就会产生死锁

'''

import threading
import time

#这个例子其实不好，因为数字不够大，即使不手动加锁结果也会一样，因为python底层默认加GIL
#不过可以展示手动加锁的过程
list1 = [0] * 10
lock = threading.Lock()

def task1():
    lock.acquire()  # 获取线程锁  (如果锁已经被其他线程拿去使用，则需要等待锁的释放)
    for i in range(len(list1)):
        list1[i] = i
        time.sleep(0.2)
        print(list1)
    lock.release()  # 释放线程锁

def task2():
    lock.acquire()
    for i in range(len(list1)):
        print('task2:',list[i])
        time.sleep(0.3)
    lock.release()

if __name__ == '__main__':
    t1=threading.Thread(target=task1)
    t2=threading.Thread(target=task2)
    t1.start()
    t2.start()


'''
输出结果：

[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 2, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 2, 3, 0, 0, 0, 0, 0, 0]
[0, 1, 2, 3, 4, 0, 0, 0, 0, 0]
[0, 1, 2, 3, 4, 5, 0, 0, 0, 0]
[0, 1, 2, 3, 4, 5, 6, 0, 0, 0]
[0, 1, 2, 3, 4, 5, 6, 7, 0, 0]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 0]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
task2: list[0]
task2: list[1]
task2: list[2]
task2: list[3]
task2: list[4]
task2: list[5]
task2: list[6]
task2: list[7]
task2: list[8]
task2: list[9]

'''

#死锁的情况 (75行有相关备注)
from threading import Thread,Lock

lockA=Lock()
lockB=Lock()
class MyThresd1(Thread):  #自定义线程
    def run(self):  #重写run方法
        if lockA.acquire():
            print(self.name,'获取A锁')  #self.name如果没有给它名字，它自己会给自己命名
            time.sleep(0.1)  #在这个位置，线程t1进入【阻塞】状态，没有到判断获取B锁的位置就转成了线程t2
            if lockB.acquire(timeout=3):  #如果括号内不加timeout，则会出现死锁的情况，为了避免这种情况，要加timeout (如果3秒内没有获取B锁，则直接返回False)
                print(self.name,'获取B锁，并保有A锁')
                lockB.release()
            lockA.release()


class MyThresd2(Thread):  #自定义线程
    def run(self):  #重写run方法
        if lockB.acquire():
            print(self.name,'获取B锁')  #self.name如果没有给它名字，它自己会给自己命名
            time.sleep(0.1)
            if lockA.acquire(): #在t1获取B锁的时候加了timeout，所以超时之后，t1放弃获取B锁，并且之后会释放A锁，所以这里能够获取A锁
                print(self.name,'获取A锁，并保有B锁')
                lockA.release()
            lockB.release()

t1=MyThresd1()
t2=MyThresd2()
t1.start()
t2.start()


'''
输出结果：

Thread-3 获取A锁
Thread-4 获取B锁
Thread-4 获取A锁，并保有B锁

'''