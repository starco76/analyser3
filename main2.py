import math
import numpy as np
import json

try:
    import mysql.connector

    conn = mysql.connector.connect(user = 'root',
                                host = 'localhost',
                                database = 'game')

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM `tbl_zarib`')
    datas = cursor.fetchall()
    lines=[float(i[0]) for i in datas]
    datas=[float(i[1]) for i in datas]
    conn.close()
except:
    with open("file.txt","r") as f:
        datas = json.loads(f.read())
    lines = np.arange(42,len(datas)+42).tolist()
data=datas

order_num = int(input("Order Number: "))
if order_num <1 or order_num>3:raise("bad Order Number")
rate=0
rate = float(input("Enter Your Number: "))
Percentage = float(input("Enter Your Percentage: "))/100


def part1(data,rate,Percentage):
    count={}
    be_cond={}
    i=1
    while i<len(data):
        pre,now = data[i-1] , data[i]
        dec_part = round(pre%1,2)
        count.update({dec_part:count.get(dec_part,0)+1})
        if now>=rate:be_cond.update({dec_part:be_cond.get(dec_part,0)+1})
        i+=1
    res={}
    for i in count: 
        if count[i]*Percentage<=be_cond.get(i,0):
            res.update({i:[count[i],be_cond.get(i,0)]})
    return res

def part2(data,rate,Percentage):
    count={}
    be_cond={}
    i=2
    while i<len(data):
        pre,now = data[i-2:i] , data[i]
        # print(pre+[now])
        sum_num = round(sum(pre),2)
        count.update({sum_num:count.get(sum_num,0)+1})
        if rate>0:cond = now>=rate
        else:cond = now<abs(rate)
        if cond:be_cond.update({sum_num:be_cond.get(sum_num,0)+1})
        i+=1
    res={}
    for i in count:
        # print(count[i]*Percentaئge , be_cond.get(i,0),count[i]*Percentage<=be_cond.get(i,0))
        if count[i]*Percentage<=be_cond.get(i,0):
            res.update({i:[count[i],be_cond.get(i,0)]})
    return res

def part3(data,rate,Percentage):
    count={}
    be_cond={}
    i=2
    while i<len(data):
        pre,now = data[i-2:i] , data[i]
        sum_dec =round(sum(list(map(lambda x:round(x%1,2),pre))),2)
        count.update({sum_dec:count.get(sum_dec,0)+1})
        if rate>0:cond = now>=rate
        else:cond = now<abs(rate)
        if cond:be_cond.update({sum_dec:be_cond.get(sum_dec,0)+1})
        i+=1
    res={}
    for i in count:
        if count[i]*Percentage<=be_cond.get(i,0):
            res.update({i:[count[i],be_cond.get(i,0)]})
    return res

if 1<=order_num<=5:
    res = '\n'
    if order_num==1:
        part=part1(data,rate,.2)
    elif order_num==2:
        part=part2(data,rate,Percentage)
    elif order_num==3:
        part=part3(data,rate,Percentage)
    
    for i in part:
        res+=str(i)+": "+str(part[i][0])+"    "+str(part[i][1])+"\n"
if rate < 0:add="Not"
else:add=""
with open("result-oreder-"+add+str(order_num),"w") as f:
    f.write(res)
