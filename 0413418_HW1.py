# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

import numpy
import pandas
import time

# 先讀檔進入棑程
fp = open("10000data_1.txt", "r")   #讀檔
array = numpy.loadtxt("10000data_1.txt")  #輸成矩陣
length=[] #排成長度
duedate=[] #到期日
for i in range(1,20001):
    if(i%2==1):
        length.append(array[i])
    else:    
       duedate.append(array[i])
oklength=sorted(length)#預備用
okduedate=sorted(duedate)#預備用

data = pandas.DataFrame({'length': length, 'duedate': duedate})#合併兩資料

# SPT algo
SPTtStart = time.time()#計時開始
sptsuccessno=0
sptfailureno=0
spt = data.sort_values(['length'],ascending=True) #排序長度
spt = spt.reset_index(drop=True)
spttotallength=0 #排程長度
sptdatalength=[]
sptdataduedate=[]
for i in range(0,10000):
    sptdatalength.append(spt.length[i])
    sptdataduedate.append(spt.duedate[i])
    sptdata = pandas.DataFrame({'length': sptdatalength, 'duedate': sptdataduedate})
    spttotallength = sum(sptdata.length)
    sptdataduedatemax = max(sptdata.duedate)
    if (spttotallength > sptdataduedatemax):
       del sptdata.length[i]
       del sptdata.duedate[i]
       sptfailureno+=1
    else:
        sptsuccessno+=1
SPTtEnd = time.time()#計時結束
print("spt可以如期完工的個數",sptsuccessno)
print("spt無法如期完工的個數",sptfailureno)
spttime = SPTtEnd - SPTtStart
print ("The SPT cost of time:",spttime)



# EDD algo
EDDtStart = time.time()#計時開始
eddsuccessno=0
eddfailureno=0
edd = data.sort_values(['duedate','length'],ascending=True) #排序到期日
edd = edd.reset_index(drop=True)
eddtotallength=0 #排程長度
for i in range(0,10000):
    eddtotallength = eddtotallength + edd.loc[i,'length']
    if (eddtotallength > edd.loc[i,'duedate']):
        eddtotallength = eddtotallength - edd.loc[i,'length']
        eddfailureno+=1
    else:
        eddsuccessno+=1
EDDtEnd = time.time()#計時結束
print("edd可以如期完工的個數",eddsuccessno)
print("edd無法如期完工的個數",eddfailureno)
eddtime = EDDtEnd - EDDtStart
print ("The EDD cost of time:" ,eddtime)