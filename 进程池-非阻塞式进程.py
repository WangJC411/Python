# -*- coding: UTF-8 -*-
'''
非阻塞式进程：
优先把全部任务添加到队列中（先不进行进程）
回调函数（callback_func）是在任务完成后调用的，task函数中需要return值
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
    return '完成{}号任务，用时{}秒,进程id：{}'.format(taskname, end - start,
                                          os.getpid())  # return值都被apply_async通过callback丢进container里了


container = []


def callback_func(n):
    container.append(n)


if __name__ == '__main__':
    pool = Pool(5)  # 设置进程最大数量为5个
    tasklist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']  # 一共有10个任务
    for maintask in tasklist:
        for i in container:  # 验证回调函数是什么时候被调用的（从输出看出，这个container里的值都是空的,所以证明callback确实是等子进程完成之后再进行的）
            print(i)
        # apply_async是非阻塞式的进程模式
        pool.apply_async(task, args=(maintask,),
                         callback=callback_func)  # args传的是任务名称，callback是指回调函数，把task中的return传到callback_func中的n变量里

    # close和join是为了拖住主进程，防止主进程结束，子进程被迫关闭
    pool.close()
    pool.join()

    for i in container:
        print(i)

'''
输出结果：

开始1号任务！
开始2号任务！
开始3号任务！
开始4号任务！
开始5号任务！
开始6号任务！
开始7号任务！
开始8号任务！
开始9号任务！
开始10号任务！
完成5号任务，用时0.7187533378601074秒,进程id：21644
完成6号任务，用时0.40622591972351074秒,进程id：21644
完成3号任务，用时1.1718697547912598秒,进程id：6176
完成1号任务，用时1.4842276573181152秒,进程id：11288
完成4号任务，用时1.6405653953552246秒,进程id：8748
完成10号任务，用时0.1406080722808838秒,进程id：8748
完成2号任务，用时1.9842779636383057秒,进程id：15200
完成8号任务，用时1.2811052799224854秒,进程id：6176
完成7号任务，用时1.8279681205749512秒,进程id：21644
完成9号任务，用时1.828031301498413秒,进程id：11288

Process finished with exit code 0

'''
