# -*- coding: UTF-8 -*-
'''
阻塞式进程：
添加一个任务，执行一个任务，前一个任务不结束，下一个任务就进不来
没有回调函数，所以task函数中不需要return值
'''

from multiprocessing import Pool
import time
from random import random
import os


def task(taskname):  # 输入任务名称
    start = time.time()  # 得到开始时间
    print('开始{}号任务！'.format(taskname))
    time.sleep(random() * 2)  # 为了防止完成任务时间一样，所以设置完成任务的随机时间
    end = time.time()  # 得到结束时间
    print('完成{}号任务，用时{}秒,进程id：{}'.format(taskname, end - start, os.getpid()))


if __name__ == '__main__':
    pool = Pool(5)  # 设置进程最大数量为5个
    tasklist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']  # 一共有10个任务
    for maintask in tasklist:
        pool.apply(task, args=(maintask,))  # args传的是任务名称

'''
输出结果：

开始1号任务！
完成1号任务，用时0.3291292190551758秒,进程id：12436
开始2号任务！
完成2号任务，用时0.5498545169830322秒,进程id：16708
开始3号任务！
完成3号任务，用时0.8009893894195557秒,进程id：11232
开始4号任务！
完成4号任务，用时0.09427165985107422秒,进程id：20992
开始5号任务！
完成5号任务，用时1.8054773807525635秒,进程id：1640
开始6号任务！
完成6号任务，用时1.695584774017334秒,进程id：12436
开始7号任务！
完成7号任务，用时1.9606740474700928秒,进程id：16708
开始8号任务！
完成8号任务，用时0.1261587142944336秒,进程id：11232
开始9号任务！
完成9号任务，用时0.07812070846557617秒,进程id：20992
开始10号任务！
完成10号任务，用时1.6165578365325928秒,进程id：1640

Process finished with exit code 0

'''
