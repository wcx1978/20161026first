# -*- coding: utf-8 -*-
'''
查找某一记录是否存在于随机库字典中。

此文件要最精减运行才行，不能占用内存等资源
'''
import time
print("请输入你要找的开奖号序列，按‘ 4 7 9 10 18 20 11 ’格式打入")
print("最后一行  5 7 12 22 23 29 10")
要找的开奖号 = str(input())

if 要找的开奖号 == None or 要找的开奖号 == '':
    print("输入为空不执行")

else:
    t1 = time.time()
    f0 = open('D:\\python-my\\py\\福彩项目准备\\RandomNo.txt','r')
    找到 = False
    for i in range(1,5000000):
        # 500万行很吃力
        字典中某行 = str(f0.readline()).strip('\n')
        print(字典中某行)
        if  字典中某行 == 要找的开奖号:
            找到 = True 
            f0.__next__
            找对号某行的下一行 = f0.readline()
            break
        else:
            f0.__next__
    if 找到 == True:
        t2 = time.time()
        print("恭喜，找到了，它的下一行是：")
        print(找对号某行的下一行)
        print('费时 %s 秒。'%str(int(t2-t1)))        
    else:
        t2 = time.time()
        print('抱歉，翻了500万条记录都没找到')
        print('费时 %s 秒。'%str(int(t2-t1)))        
