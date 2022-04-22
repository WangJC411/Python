# -*- coding: UTF-8 -*-
# 生成器
'''
生成器可以应用在多任务协程，例如有两个for循环，正常情况下是先完成一个for循环，才进行下一个for循环。
(加入yield暂停和next()开始)利用生成器可以让第一个循环跑一圈，再让第二个循环跑一圈，再让第一个循环跑一圈，交替进行
'''

g = (x * 3 for x in range(20))
# g.__next__() 和 next(g) 效果相等，都是打印下一个g中的值出来，一次打印一个结果，如果超过g所拥有的数量，就会报错
print(g.__next__())  # 0
print(g.__next__())  # 3
print(g.__next__())  # 6
print(next(g))  # 9
print(next(g))  # 12
print(next(g))  # 15

'''
输出结果：

0
3
6
9
12
15

'''

gg = (x * 3 for x in range(20))
while True:
    try:
        print(next(gg))
    except:  # 超过范围，捕获异常，退出循环
        print('ending')
        break
'''
输出结果：

0
3
6
9
12
15
18
21
24
27
30
33
36
39
42
45
48
51
54
57
ending

'''


def fib(length):
    a, b = 0, 1
    n = 0
    while n < length:
        yield b  # yield 有return+暂停的作用(有了yield就是生成器，调用时需要去接收)
        a, b = b, a + b  # a,b 可以同时赋值
        n += 1
    return '没有更多值'


f = fib(8)
while True:
    try:
        print(next(f))
    except Exception as err:
        print(err)
        break
'''
输出结果：

1
1
2
3
5
8
13
21
没有更多值

'''


def gen():
    i = 0
    while i < 5:
        temp = yield i
        print('temp:', temp)
        i += 1
    return '没有更多数据'


g = gen()
print(g.send(None))  # 第一次执行生成器不能send值
n1 = g.send('aaa')  # send有启动生成器的功能
print('n1:', n1)
n2 = g.send('bbb')
print('n2:', n2)

'''
输出结果：

0
temp: aaa
n1: 1
temp: bbb
n2: 2

'''

'''
最后一部分的debug过程：
    print(g.send(None))  # (output: 0) yield i = 0,此时还没有给temp赋值 
    n1=g.send('aaa')   #(output: temp:aaa) n1 = i = 1, temp = aaa ,给temp赋值(aaa)，执行while里的print后，开始第二圈，直到yield的位置暂停
    print('n1:',n1)     #(output: n1:1)  n1 = i = 1 , temp = aaa 
    n2=g.send('bbb')    #(outpupt: temp:bbb)  n1 = i = 2 ,temp = bbb ,给temp赋值(bbb),执行while里的print，开始第三圈，直到yield的位置暂停
    print('n2:',n2)     #(output: n2:2)  n2 = i = 2 ,temp = bbb

'''

'''
迭代器：
可以被next()函数调用并不断返回下一个值的对象称为迭代器
list是可迭代对象，但不是迭代器
可以通过iter(list)把list转成迭代器
生成器本身就是一种迭代器

'''
