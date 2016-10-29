# -*- coding: utf-8 -*-
 
'''
# 随机生成相关

import random


aa = random.randint(1,200)   #指定整出范围 内生成
cc = random.randrange(width) #0-范围内生成
bb = 

aa = [1,2,3]
random.shuffle(aa) #洗牌
print(aa)

temp = random.choice(RedBoll)

'''

import random
import time

def 生成一组号码():
    RedBoll = list(range(1,33))
    Resualt = []
    for i in range(0,6):
        temp = random.choice(RedBoll)
        Resualt.append(temp)
        del RedBoll[RedBoll.index(temp)]
    Resualt.sort()
    BlueBoll = list(range(1,16))
    Resualt.append(random.choice(BlueBoll))
    return Resualt

#for i in range(1,1000):
#    print(生成一组号码())

t1 = time.time()
print("开始计时",'-'*50)
Ra = []
for i in range(1,500000):
    # 一千条内不易重，一万就会出重
    temp = 生成一组号码()
    if temp in Ra:
        # print("已存在",temp)
    else:
        # 不重复的才放入
        Ra.append(temp)
'''
print('-'*40)
print('原生的')        
for i in Ra:
    print(i)
    
print('-'*40)
print('整齐的')        
Ra.sort()
for i in Ra:
    print(i)
    
print('-'*40)    
print('打乱的')
random.shuffle(Ra)
for i in Ra:
    print(i)
'''

print("写文件",'-'*50)

f0 = open('D:\\python-my\\py\\福彩项目准备\\RandomNo.txt','w')
for i in Ra:
    ttt = str(i)
    ttt = ttt.replace('[','')
    ttt = ttt.replace(']','')
    ttt = ttt.replace(',','')
    f0.write(ttt+'\n')
    f0.__next__
f0.close()


t2 = time.time()
print(t1,' - ',t2)
print('生成500万行费时_%s_秒。'%str(t2-t1))

#
# 读回来
f0 = open('D:\\python-my\\py\\福彩项目准备\\RandomNo.txt','r')
bb = []
for line in f0:
    rr = f0.readline()
    LL = rr.split()
    bb.append(LL)

print(bb)
    
