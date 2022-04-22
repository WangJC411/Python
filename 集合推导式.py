# -*- coding: UTF-8 -*-
# 列表推导式
'''
1、从原列表取值：
    newlist = [x for x in list]  第一个x是指输出表达式
2、有if条件取值：
    newlist = [x for x in list if ...]   有if条件，满足条件就可取出
3、有if-else条件：
    newlist = [x+100 if x%3 == 0 else x-100 for x in range(1,101)]
'''

list = [1, 2, 3, 4, 5, 6, 7]
newlist = [x for x in list]
print(newlist)

newlist = [x + 1 if x % 3 == 0 else x - 1 for x in range(1, 20)]
print(newlist)
# 若有两个变量，可以用在一个推导式中用两个for
newlist = [(x, y) for x in range(5) if x % 2 == 0 for y in range(10) if y % 2 != 0]
print(newlist)

# 集合推导式和字典推导式跟列表推导式相似，只是换成了大括号
newset = {x for x in range(50) if x % 5 == 0}
print(newset)

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
newdict = {value: key for key, value in dict1.items()}  # 把dict1中的key和value互换
print(newdict)

'''
输出结果：；

[1, 2, 3, 4, 5, 6, 7]
[0, 1, 4, 3, 4, 7, 6, 7, 10, 9, 10, 13, 12, 13, 16, 15, 16, 19, 18]
[(0, 1), (0, 3), (0, 5), (0, 7), (0, 9), (2, 1), (2, 3), (2, 5), (2, 7), (2, 9), (4, 1), (4, 3), (4, 5), (4, 7), (4, 9)]
{0, 35, 5, 40, 10, 45, 15, 20, 25, 30}
{1: 'a', 2: 'b', 3: 'c', 4: 'd'}

'''
