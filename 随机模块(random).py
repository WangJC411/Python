# -*- coding: UTF-8 -*-
# 随机模块

import random

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
a = random.random()  # 0~1之间的随机数
b = random.randrange(1, 10, 2)  # 1~10之间整数，步长为2(间隔为1)，不包括10
c = random.randint(1, 10)  # 1~10之间整数，包括10
d = random.choice(list1)  # 从list1中随机挑选一个
random.shuffle(list1)  # 打乱列表中的顺序
print('0~1之间的随机数:', a)
print('1~10之间整数，步长为2(间隔为1)，不包括10:', b)
print('1~10之间整数，包括10:', c)
print('从list1中随机挑选一个:', d)
print('打乱列表中的顺序:', list1)

'''
输出结果：(结果不固定)

0~1之间的随机数: 0.8230507766786873
1~10之间整数，步长为2(间隔为1)，不包括10: 5
1~10之间整数，包括10: 6
从list1中随机挑选一个: a
打乱列表中的顺序: ['a', 'f', 'c', 'g', 'b', 'd', 'e']
'''
