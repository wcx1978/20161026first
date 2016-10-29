# -*- coding: utf-8 -*-
'''
此文件要最精减运行才行，不能占用内存等资源
'''
import random
import time

def 生成一组号码():
    全部红球 = list(range(1,33))
    选出结果 = []
    for i in range(0,6):
        temp = random.choice(全部红球)
        选出结果.append(temp)
        del 全部红球[全部红球.index(temp)]
    选出结果.sort()
    全部蓝球 = list(range(1,16))
    选出结果.append(random.choice(全部蓝球))
    return 选出结果

t1 = time.time()
print("开始计时",'-'*50)

Ra = []
f0 = open('D:\\python-my\\py\\福彩项目准备\\RandomNo.txt','w')
for i in range(1,5000000):
    # 一千条内不易重，一万就会出重， 5百万试68秒94M大小
    temp = str(生成一组号码())
    temp = temp.replace('[','')
    temp = temp.replace(']','')
    temp = temp.replace(',','')
    f0.write(temp.rstrip() + '\n')
    f0.__next__
    # 这样生成一行写一行可能会重复的
print("写 文 件",'-'*50)

f0.close()

t2 = time.time()
print('这电脑生成500万行费时 %s 秒。'%str(int(t2-t1)))





