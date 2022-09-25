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
    # datas=[1.19,1.35,1.33,1.08,4.41,7.61,2.18,2.68,73.38,1.00,2.20,2.77,1.14,1.35,1.31,1.77,2.98,3.59,9.64,4.01,3.98,2.75,1.02,1.67,3.02,1.25,3.30,4.60,1.29,89.09,1.32,4.57,1.00,1.27,10.97,3.82,3.18,1.59,1.34,27.73,23.98,1.76,1.52,1.56,1.51,2.07,2.96,2.19,13.13,1.44]
    datas=[1.43 , 2.00  ,3.10 , 1.43  ,1.00  ,1.10  ,2.33, 2.20,  1.00 , 1.43  ,2.00  ,3.10 , 2.53 , 2.00  ,2.53 , 6.3 , 3.53 , 1.00  ,8.20]
    lines = np.arange(42,len(datas)+42).tolist()
    # print("error")
    # input("...")
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
    mx_=0
    for i in count:
        if count[i]!=0:
            if be_cond.get(i,0)/count[i] >mx_:
                mx_ = round(be_cond.get(i,0)/count[i]*100)
        if count[i]*Percentage<=be_cond.get(i,0):
            res.update({i:[count[i],be_cond.get(i,0)]})
    loss = 0
    mx_loss=100000
    i=1
    
    while i<len(data):
        pre,now = data[i-1] , data[i]
        dec_part = round(pre%1,2)
        if dec_part in res:
            if now>=rate:
                loss+=rate-1
            else:loss-=1
        if loss<mx_loss:mx_loss=loss
        

        i+=1
    new_mx_loss = new_mx_losses(data,res,res,1)

    if len(res)==0:
        res.update({"min":[0,mx_]})
    return res,res,mx_loss,new_mx_loss

def part2(data,rate,Percentage):
    count={}
    be_cond={}
    i=2
    while i<len(data):
        pre,now = data[i-2:i] , data[i]
        sum_num = round(sum(pre),2)
        count.update({sum_num:count.get(sum_num,0)+1})
        if rate>0:cond = now>=rate
        else:cond = now<abs(rate)
        if cond:be_cond.update({sum_num:be_cond.get(sum_num,0)+1})
        i+=1

    res={}
    mx_=0
    out= {}
    for i in count:
        
        if count[i]!=0:
            if be_cond.get(i,0)/count[i] >mx_:
                mx_ = round(be_cond.get(i,0)/count[i]*100)
        if count[i]*Percentage<=be_cond.get(i,0):
            if count[i]>1:out.update({i:count[i]})
            res.update({i:[count[i],be_cond.get(i,0)]})
    if len(res)>0:
        i=2
        loss = 0
        mx_loss=0
        while i<len(data):
            pre,now = data[i-2:i] , data[i]
            sum_num = round(sum(pre),2)
            if sum_num in res:
                if now>=abs(rate):loss+=rate-1
                else:loss-=1
            if loss<mx_loss:mx_loss=loss
            i+=1

    new_mx_loss = new_mx_losses(data,res,out,2)
    if len(res)==0:
        res.update({"min":[0,mx_]})
    return res,out,mx_loss,new_mx_loss

    
def new_mx_losses(data,res,out, ii=1):
    i=ii
    new_loss = 0
    new_mx_loss=0
    while i<len(data):
        pre,now = data[i-ii:i] , data[i]
        sum_num = round(sum(pre),2)
        if sum_num in out:
            part= res.get(sum_num)
            profit = round((part[1]*(rate-1))-(part[0]-part[1]),2)
            if profit>0:
                if now>=abs(rate):
                    new_loss+=rate-1
                else:new_loss-=1
        if new_loss<new_mx_loss:new_mx_loss=new_loss
        i+=1
    return new_mx_loss

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
    mx_=0
    for i in count:
        if count[i]!=0:
            if be_cond.get(i,0)/count[i] >mx_:
                mx_ = round(be_cond.get(i,0)/count[i]*100)
        if count[i]*Percentage<=be_cond.get(i,0):
            res.update({i:[count[i],be_cond.get(i,0)]})
    i=2
    loss = 0
    mx_loss=0
 
    while i<len(data):
        pre,now = data[i-2:i] , data[i]
        
        if sum_dec in res:
            if now>=abs(rate):loss+=rate-1
            else:loss-=1
            
            if loss<mx_loss:mx_loss=loss

        i+=1
    new_mx_loss = new_mx_losses(data,res,res,2)
    if len(res)==0:
        res.update({"min":[0,mx_]})
    return res,res,mx_loss,new_mx_loss

if 1<=order_num<=5:
    res = '\n'
    if order_num==1:
        part,base,mx_loss,new_loss=part1(data,rate,Percentage)
    elif order_num==2:
        part,base,mx_loss,new_loss=part2(data,rate,Percentage)
    elif order_num==3:
        part,base,mx_loss,new_loss=part3(data,rate,Percentage)
    filter =[]
    total = 0
    for i in part:
        profit = round((part[i][1]*(rate-1))-(part[i][0]-part[i][1]),2)
        if profit <=0:filter+=[i]

        if profit>0 and part[i][0]>1:total+=profit
        res+=str(i)+": "+str(part[i][0])+"  ,  "+str(part[i][1])+"  ,  "+str(profit)+"\n"
    bres=""
    for i in base:
        if i not in filter:
            bres+=str(i)+","

    bres+="\n\n Total Profit ="+str(round(total,2))
    bres+="\n\n max loss ="+str(round(mx_loss,2))
    bres+="\n\n new max loss ="+str(round(new_loss,2))

if rate < 0:add="Not"
else:add=""
with open("result-oreder-"+add+str(order_num)+".txt","w") as f:
    f.write(res)

with open("result-oreder-"+add+str(order_num)+"_numbers.txt","w") as f:
    f.write(bres)