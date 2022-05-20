# -*- coding: UTF-8 -*-
#异常捕获
'''
原本会报错而被迫停止的程式，把报错收集起来，继续运行程式
形式：
    try：
        有可能产生多种异常
        return 0
    except 异常类型 1：
        ...
        return 1
    except 异常类型 2：
        ...
        return 2
    except Exception as err:  #把错误内容用err表示
        print(err)   #打印具体错误类型
        return 3
    else：   #try中的程式没有报错才会进来的程式
        ...
        return 4
    finally：
        return 5

底层逻辑(这部分比较复杂，有需要的时候要再捡起来学才行)：
    1、try中有return，无异常，则else不执行，finally执行(若finally中有return值，则返回finally里的return值；若无，则返回try中的return值)
    2、try中无return，无异常，则else执行，finally执行(若finally中有return值，则返回finally里的return值；若无，则返回else中的return值)
    3、try中有/无return，有异常，则else不执行，except执行，finally执行(若finally中有return值，则返回finally里的return值；若无，则返回except中的return值)

'''

#除了系统自带的错误之外，也可以自己手动触发错误(自己设定错误)

def register():
    username=input('输出用户名(长度超过6位)：')
    if len(username)<6:
        raise Exception('用户名长度必须6位以上！')  #手动触发异常，命名这个错误为'用户名长度必须6位以上！'
    else:
        print('输入的用户名为 ',username)


try:
    register()
except Exception as err:
    print(err)
    print('注册失败')
else:
    print('注册成功')


'''
输出结果：

输出用户名(长度超过6位)：sd
用户名长度必须6位以上！
注册失败

'''