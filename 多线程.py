# -*- coding: UTF-8 -*-
# 多线程
'''
线程是依赖进程的，多个线程共用一个进程的资源，轮流使用，切换速度很快，所以使用者不会察觉有在切换
线程占用的是进程的资源，所以占用资源比较少
线程的状态：【新建】-->【就绪】-->【运行】  -->【结束】
                                     -->【阻塞】(遇到sleep时，会先把资源空出来给其他线程使用，它自己进入阻塞状态)-->【就绪】
*线程可以共享全局变量*

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
    下面有具体的例子

线程用于耗时的操作
进程用于计算密集型的操作





'''

import threading
from time import sleep


def download(n):
    imagelist = ['A', 'B', 'C', 'D']
    for image in imagelist:
        print('正在下载：', image)
        sleep(n)
        print('下载完成：', image)


def listenmusic():
    musiclist = ['aaa', 'bbb', 'ccc', 'ddd']
    for music in musiclist:
        print('正在听歌：', music)
        sleep(2)


# 线程的新建和启动跟进程一样
tt1 = threading.Thread(target=download, name='download', args=(1,))  # 子线程
tt1.start()
tt2 = threading.Thread(target=listenmusic, name='listen music')
tt2.start()

'''
输出结果：

正在下载： A
正在听歌： aaa
下载完成： A
正在下载： B
正在听歌： bbb
下载完成： B
正在下载： C
下载完成： C
正在下载： D
正在听歌： ccc
下载完成： D
正在听歌： ddd

'''

# 数字不大的情况
sleep(8)
ticket = 1000

#run1 和 run2 程式内容是一样的，用的都是全局变量ticket
def run1():
    global ticket
    for i in range(100):
        ticket -= 1


def run2():
    global ticket
    for i in range(100):
        ticket -= 1

t1=threading.Thread(target=run1,name='t1')
t2=threading.Thread(target=run2,name='t1')
t3=threading.Thread(target=run1,name='t1')
t4=threading.Thread(target=run2,name='t1')

t1.start()
t2.start()
t3.start()
t4.start()
# t1.join()
# t2.join()
# t3.join()
# t4.join()
print(ticket)

#输出结果：  600
#因为线程是可以使用全局变量的，所以每个线程都是在共用一个ticket变量，每个线程都都减少100，一共减少400，所以结果是600


#数字较大的情况 (GIL被释放)

q=0
def task1():
    global q
    for i in range(1000000):
        q+=1
    print('task1 的q值为：',q)

def task2():
    global q
    for i in range(1000000):
        q+=1
    print('task2 的q值为：',q)

q1=threading.Thread(target=task1)
q2=threading.Thread(target=task2)
q1.start()
q2.start()
q1.join()
q2.join()

'''
输出结果：
task1 的q值为： 1975581   #这个值应该是2000000，但因为GIL被释放，所以出现数据不安全的情况
task2 的q值为： 2000000   #这个值按道理也会出错，但不知道为什么它是正确的...

'''