# -*- coding: UTF-8 -*-
#生产者与消费者
import queue
import random
import threading
import time


def produce(q):
    i = 0
    while i<10:
        num = random.randint(1,100)
        q.put(num)
        print('生产者产生数据：',num)
        time.sleep(0.2)
        i+=1
    q.put(None)
    q.task_done() #完成任务

def consume(q):
    while True:
        item=q.get()
        if item is None:
            break
        print('消费者获取到数据：',item)
        time.sleep(0.5)
    q.task_done()

q=queue.Queue(10)
arr=[]
tp=threading.Thread(target=produce,args=(q,))
tp.start()
tc=threading.Thread(target=consume,args=(q,))
tc.start()

'''
输出结果：

生产者产生数据： 74
消费者获取到数据： 74
生产者产生数据： 80
生产者产生数据： 57
消费者获取到数据： 80
生产者产生数据： 93
生产者产生数据： 22
消费者获取到数据： 57
生产者产生数据： 52
生产者产生数据： 73
生产者产生数据： 10
消费者获取到数据： 93
生产者产生数据： 41
生产者产生数据： 35
消费者获取到数据： 22
消费者获取到数据： 52
消费者获取到数据： 73
消费者获取到数据： 10
消费者获取到数据： 41
消费者获取到数据： 35

'''