# -*- coding: UTF-8 -*-
#单例模式
'''
第一次调用一个类时，会创建一个内存地址，之后再调用时，都会共用这个内存地址，以起到节约内存的作用
(适用于只是想用一个类中某些功能，但没必要另外创建对象的情况)

'''

class Single:
    __instance=None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:  #判断是否已经有地址了，若没有，则产生一个新的地址，若有，则直接返回之前的地址
            cls.__instance=object.__new__(cls)   #odject.__new__(cls) 产生一个内存地址
            return cls.__instance
        else:
            return cls.__instance

s1=Single()
s2=Single()
#打印两个变量的地址，会发现他们用的地址是同一个地址
print(s1)
print(s2)


'''
输出结果：

<__main__.Single object at 0x0000024DCF13BF10>
<__main__.Single object at 0x0000024DCF13BF10>

'''