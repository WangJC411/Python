# -*- coding: UTF-8 -*-
'''
正则模块：
import re
re.match(pattern,msg)  从头开始匹配，一开始不出现就算没有匹配到  pattern 配对字符 ， msg 匹配内容
re.search(pattern,msg)  对整个字符串匹配，找到第一个符合的
re.findall(pattern ,msg)  对整个字符进行匹配，找到所有符合的内容
re.sub(pattern,x,msg)  在匹配内容中找到配对字符，把它替换成x
re.split(x,msg)  把匹配内容根据x进行划分(以x作为分隔符)

正则常用字符：
1、基础
    . 任意字符
    [] 范围
    | 或
    () 一组
2、量词
    * >=0
    + >=1
    ? 0 or 1
    {m} =m
    {m,} >=m
    {m,n} >=m and <=n
3、预定义
    \s space
    \S not space
    \d digit
    \D not digit
    \w word (0-9a-zA-Z_)
    \W not word
4、分组
    ()--->group()
    a、number
        (\w+)(w\d+)---->(group1)(group2)
        \1 , \2 表示引用前面的内容
    b、name
        (?P<name>\w+) 命名
        (?P=name) 引用

补充：
贪婪模式：
    默认是贪婪的---->总是匹配尽可能多的字符
    在原本的符号后面加？变成非贪婪---->总是匹配尽可能少的字符

'''
import re


def func(temp):
    num = temp.group()
    num1 = int(num) + 1
    return str(num1)


result = re.sub(r'\d+', func, 'java:99,python:92')  # 把字符中所有的数字都按照func中的规则加一
print(result)

# 贪婪模式例子
msg = 'abc123def'
result = re.match(r'abc(\d+)', msg)  # 贪婪模式
print(result)  # 匹配到的结果是: abc123
result = re.match(r'abc(\d+?)', msg)  # 非贪婪模式
print(result)  # 匹配到的结果是: abc1

'''
输出结果：

java:100,python:93
<re.Match object; span=(0, 6), match='abc123'>
<re.Match object; span=(0, 4), match='abc1'>

'''
