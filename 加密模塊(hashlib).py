# -*- coding: UTF-8 -*-
# 加密模块(hashlib)
'''
md5,SHA1,SHA224,SHA256等加密方式只能加密，不能解密(单向操作)
用在登录账号密码配对时，要把匹配的东西通过用一种加密方式加密后，把加密结果与之前的比较,若结果一致则代表密码正确

BASE64可以加密和解密(可双向操作)
'''
import hashlib

msg = '加密内容'
md5 = hashlib.md5(msg.encode('UTF-8'))  # md5是加密类型（加密方法），加密中文需要加UTF-8
result = md5.hexdigest()  # 把加密结果转成16进制的字符串形式
print(result)  # ‘加密内容’ 这四个字加密成16进制字符串

'''
输出结果：
220be55b2e3d8e60f9214b04a7a2328f
'''
