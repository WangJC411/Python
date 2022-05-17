# -*- coding: UTF-8 -*-
# 文件操作
'''
open(r'绝对路径或相对路径' ,'打开方式',enconding='UTF-8')  若文件內有中文，需要加enconding='UTF-8'
打开方式：
    r:以只讀方式開啟檔案。檔案的指標將會放在檔案的開頭。這是預設模式
    w:開啟一個檔案只用於寫入。如果該檔案已存在則將其覆蓋。如果該檔案不存在，建立新檔案。
    a:開啟一個檔案用於追加。如果該檔案已存在，檔案指標將會放在檔案的結尾。也就是說，新的內容將會被寫入到已有內容之後。如果該檔案不存在，建立新檔案進行寫入。
    rb:以二進位制格式開啟一個檔案用於只讀。檔案指標將會放在檔案的開頭。這是預設模式。
    wb:以二進位制格式開啟一個檔案只用於寫入。如果該檔案已存在則將其覆蓋。如果該檔案不存在，建立新檔案。
    ab:以二進位制格式開啟一個檔案用於追加。如果該檔案已存在，檔案指標將會放在檔案的結尾。也就是說，新的內容將會被寫入到已有內容之後。如果該檔案不存在，建立新檔案進行寫入。
    r+:開啟一個檔案用於讀寫。檔案指標將會放在檔案的開頭。
    w+:開啟一個檔案用於讀寫。如果該檔案已存在則將其覆蓋。如果該檔案不存在，建立新檔案。
    a+:開啟一個檔案用於讀寫。如果該檔案已存在，檔案指標將會放在檔案的結尾。檔案開啟時會是追加模式。如果該檔案不存在，建立新檔案用於讀寫。
    rb+:以二進位制格式開啟一個檔案用於讀寫。檔案指標將會放在檔案的開頭
    wb+:以二進位制格式開啟一個檔案用於讀寫。如果該檔案已存在則將其覆蓋。如果該檔案不存在，建立新檔案。
    ab+:以二進位制格式開啟一個檔案用於追加。如果該檔案已存在，檔案指標將會放在檔案的結尾。如果該檔案不存在，建立新檔案用於讀寫。

stream = open(r'C:\desktop\test.txt',enconding='UTF-8')  這邊stream可以理解為開啟一種通道(需要手動關閉這個通道)，下面的事情要在這個通道內進行
container = stream.read()  在通道內讀取內容
ab = stream.readlines()     可讀性(返回值是True/False)
line = stream.readline()  只讀一行內容
lines = stream.readlines()  讀出的內容保存在一個列表(lines)裡
result = stream.write('xxx')    在通道內寫入內容
result = stream.writelines(['xxx/n','yyy/n','zzz/n'])  寫入多行文字，需要手動添加/n換行
stream.close()  關閉通道
with open(r'絕對路徑/相對路徑','打開方式',enconding='UTF-8') as wstream：    這個方式在縮進的範圍內會開啟通道，出了縮進的範圍就自動關閉通道
    pass

path = os.path.dirname(文件路徑/當前文件：__file__)  獲取當前py文件的路徑(不包括文件名)，可以通過這方式獲取去掉文件名的路徑
例如:    path = os.path.dirname(r'C:/Users\Wang\Desktop\硕士班\Python\image\three dogs.jpg')
會得到：  C:/Users\Wang\Desktop\硕士班\Python\image
pathfile = os.path.join(path,'AA.jpg')  在path這個路徑上添加AA.jpg (可以添加很多路徑)
path = os.path.abspath('aa.txt') 獲取文件的絕對路徑 (好像只是把文件名添加到當前文件的路徑上，即使這個文件不存在也可以打印出路徑)
path = os.getcwd() 獲取當前絕對路徑(不包括文件名)，可以通過os.chdir切換
result = os.path.split(絕對路徑)  把文件名和路徑分開，放到一個元組裡面
result = os.path.splitext(絕對路徑)  把文件類型(.py .txt)和剩下的分開
size = os.path.getsize(絕對路徑)  獲取文件字節數大小
dir = os.listdir(絕對路徑)  獲取指定目錄下的所有文件和文件夾(以列表的形式)
os.mkdir(絕對路徑+文件夾名)  在指定路徑上創建文件夾(若已存在，則會報錯)
os.path.exists(絕對路徑+文件夾名)   判斷是否存在這個文件
os.rmdir(絕對路徑+文件夾名)  刪除空文件夾，不是空文件夾不能被刪除
os.path.remove(絕對路徑+文件名)   刪除文件
os.chdir(絕對路徑)  切換目錄
os.path.isdir(絕對路徑)   判斷是否為目錄(文件夾)


'''

import os
#複製一張圖片
with open(r'C:\Users\Wang\Desktop\硕士班\Python\image\three dogs.jpg', 'rb') as rstream:
    container = rstream.read()
    file = rstream.name  #打開的文件的路徑(包括文件名)
    print('打開的文件的路徑(包括文件名):',file)
    file_name = file[file.rfind('\\') + 1:]  # rfind是指在file的字符串中找到最後一個符合條件的字符的位置，+1代表下一個位置，：代表從這個位置到最後
    print(file_name)
    path1 = os.path.dirname(__file__)  # 獲取當前py文件的路徑
    print("獲取當前py文件的路徑:",path1)
    pathfile = os.path.join(path1, file_name)  # 把文件名加到當前py文件路徑的後方
    print('把文件名加到當前py文件路徑的後方:',pathfile)
    with open(pathfile, 'wb') as wstream:
        wstream.write(container)
'''
輸出結果：

打開的文件的路徑(包括文件名): C:/Users\Wang\Desktop\硕士班\Python\image\three dogs.jpg
three dogs.jpg
獲取當前py文件的路徑: C:/Users\Wang\Desktop\硕士班\Python/Note
把文件名加到當前py文件路徑的後方: C:/Users\Wang\Desktop\硕士班\Python/Note\three dogs.jpg

(這段代碼主要是把three dogs.jpg這張圖片複製到當前py文件這個路徑之下)

'''


#刪除文件夾(文件夾內有東西的情況)
path = r'C:\Users\Wang\Desktop\硕士班\Python\python程式\测试文件夹2'
def removefile(path):
    filelist=os.listdir(path)  #找出目錄裡面的內容
    for file in filelist:
        path1= os.path.join(path,file) #把絕對路徑+文件名的形式組合到一起
        if os.path.isdir(path1):  # 判斷這個路徑是否為一個目錄，也就是出现文件夹里还有一个文件夹的情况
            removefile(path1)
        else:
            os.remove(path1)
    else:
        os.rmdir(path)
        print("刪除成功！")

removefile(path)

