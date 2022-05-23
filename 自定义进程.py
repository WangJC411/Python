# -*- coding: UTF-8 -*-
# 自定义进程

from multiprocessing import Process
import time

class Myprocess(Process): #在原本Process模块的基础上改写
    def __init__(self, name):
        super(Myprocess, self).__init__() #把父类的__init__搬过来
        self.name = name #再另外加上name的变量

    # 重写run方法
    def run(self):
        n = 1
        while True:
            time.sleep(0.6)
            print('{}-->自定义进程，n:{}'.format(n, self.name))
            n += 1


if __name__ == '__main__':
   p1=Myprocess('task1') #传递任务名称到self.name里
   p1.start() #这行代码会做两个动作：1、开一个进程 2、运行run()程式
   time.sleep(0.3) #把两个task隔开，不然他们的输出时间会重叠，输出结果也会重叠
   p2 = Myprocess('task2')  # 传递任务名称到self.name里
   p2.start()  # 这行代码会做两个动作：1、开一个进程 2、运行run()程式

'''
输出结果：

1-->自定义进程，n:task1
1-->自定义进程，n:task2
2-->自定义进程，n:task1
2-->自定义进程，n:task2
3-->自定义进程，n:task1
3-->自定义进程，n:task2
4-->自定义进程，n:task1
4-->自定义进程，n:task2
5-->自定义进程，n:task1
5-->自定义进程，n:task2
6-->自定义进程，n:task1
6-->自定义进程，n:task2
7-->自定义进程，n:task1
7-->自定义进程，n:task2
8-->自定义进程，n:task1
8-->自定义进程，n:task2
9-->自定义进程，n:task1
9-->自定义进程，n:task2
10-->自定义进程，n:task1
10-->自定义进程，n:task2
11-->自定义进程，n:task1
'''