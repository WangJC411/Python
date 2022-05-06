# -*- coding: UTF-8 -*-
# 队列(Queue)
'''
q.put() 往队列里面添加内容，如果队列满了，则只能等待，等到队列有空位，再添加进去
q.put('F',timeout=3)  timeout=3 代表等待3秒，如果添加不进去，则直接报错
q.qsize()  列印出队列中已有内容的数量
q.full()  用True和False值返回队列是否已满
q.get()  往队列里面取出内容，取出的顺序按照放入的顺序进行(A-B-C-D-E)，如果没有东西可以取，就一直等着
q.get(timeout=3)  跟put时一样，timeout=3 代表等待3秒，如果没东西可以取出来，则直接报错
q.put_nowait('D')  不等待，如果队列满了，则直接报错
q.get_nowait()  不等待直接取得，如果没有东西则直接报错
'''

from multiprocessing import Queue, Process
from time import sleep

q = Queue(5)  # 设置队列最多容纳数量为5个
q.put('A')  # 往队列里面添加内容，如果队列满了，则只能等待，等到队列有空位，再添加进去
q.put('B')
print(q.qsize())  # 列印出队列中已有内容的数量
q.put('C')
q.put_nowait('D')  # 不等待，如果队列满了，则直接报错
q.put('E')  # 队列已满
if not q.full():  # q.full() 用True和False值返回队列是否已满
    q.put('F', timeout=3)  # timeout=3 代表等待3秒，如果添加不进去，则直接报错
else:
    print('队列已满!')

print(q.get())  # 往队列里面取出内容，取出的顺序按照放入的顺序进行(A-B-C-D-E)，如果没有东西可以取，就一直等着
print(q.get())
print(q.get())
print(q.get())
print(q.get_nowait())  # 不等待直接取得，如果没有东西则直接报错
# print(q.get(timeout=3))  # 跟put时一样，timeout=3 代表等待3秒，如果没东西可以取出来，则直接报错

'''
输出结果：

2
队列已满!
A
B
C
D
E
报错：3秒后报错，因为33行没有可以取得内容，timeout结束后，就会直接报错

'''


def download(task):
    images = ['A', 'B', 'C', 'D', 'E', 'F', 'G']  # 用于模拟文件，可以用实际的文件操作练习
    for image in images:
        print('正在下载：', image)
        sleep(0.5)  # 模擬下載時所花的時間
        task.put(image)


def getfile(task):
    while True:
        try:
            file = task.get(timeout=3)
            print('{}保存成功！'.format(file))
        except:
            break


if __name__ == '__main__':
    task = Queue(3)
    p1 = Process(target=download, args=(task,))
    p2 = Process(target=getfile, args=(task,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

'''
輸出結果：

正在下载： A
正在下载： B
A保存成功！
正在下载： C
B保存成功！
正在下载： D
C保存成功！
正在下载： E
D保存成功！
正在下载： F
E保存成功！
正在下载： G
F保存成功！
G保存成功！

'''
