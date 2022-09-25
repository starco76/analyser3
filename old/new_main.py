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
datas=[datas]

order_num = int(input("Order Number: "))
if order_num <1 or order_num>8:raise("bad Order Number")
rate=0
if order_num!=8:
    rate = float(input("Enter Your Number: "))

def arive_counter(data,j,rate):
    c=0
    for i in range(j,len(data)):
        c+=1
        if data[i] >=rate:break
    return c , i

def calc_dec_last(inp):
    return int("{:.2f}".format(round(inp,2))[-1])

def check_reverse(in1,in2):
    return "{:.2f}".format(round(in1,2))[-2:] =="{:.2f}".format(round(in2,2))[-2:][::-1]

def part1(data,rate):
    c= 0
    big_equal=0
    get_arrive=[]
    gar= 0
    i=1
    while i<len(data)-1:
        pre,now,last = data[i-1:i+2]
        if pre==now:
            c+=1
            if last!=1 and rate<=last:
                i+=1
                big_equal+=1
            else:
                arive_counter_data = arive_counter(data,i+1,rate)
                i = arive_counter_data[1]
                get_arrive+=[arive_counter_data[0]]
        i+=1

    if len(get_arrive)>0:gar = max(get_arrive)
    return c, big_equal , gar

def part2(data,rate):
    c= 0
    big_equal=0
    get_arrive=[]
    gar= 0
    i=1
    while i<len(data)-3:
        pre,now,nxt1,nxt2,last = data[i-1:i+4]
        if pre>=2 and now>=2 and nxt1<2 and nxt2<2 and int(nxt1*10)==int(nxt2*10):
            c+=1
            if last!=1 and rate<=last:
                i+=1
                big_equal+=1
            else:
                arive_counter_data = arive_counter(data,i+1,rate)
                i = arive_counter_data[1]
                get_arrive+=[arive_counter_data[0]]
        i+=1

    if len(get_arrive)>0:gar = max(get_arrive)
               
    return c, big_equal , gar

def part3(data,rate):
    c= 0
    big_equal=0
    get_arrive=[]
    gar= 0
    i=1
    while i<len(data)-1:
        pre,now,last = data[i-1:i+2]
        if calc_dec_last(pre)%2 ==0 and calc_dec_last(now)%2==0:
            c+=1
            if last!=1 and rate<=last:
                i+=1
                big_equal+=1
            else:
                arive_counter_data = arive_counter(data,i+1,rate)
                i = arive_counter_data[1]
                get_arrive+=[arive_counter_data[0]]
        i+=1

    if len(get_arrive)>0:gar = max(get_arrive)
               
    return c, big_equal , gar

def part4(data,rate):
    c= 0
    big_equal=0
    get_arrive=[]
    gar= 0
    i=1
    while i<len(data)-1:
        pre,now,last = data[i-1:i+2]
        if calc_dec_last(pre)%2 !=0 and calc_dec_last(now)%2!=0:
            c+=1
            if last!=1 and rate<=last:
                i+=1
                big_equal+=1
            else:
                arive_counter_data = arive_counter(data,i+1,rate)
                i = arive_counter_data[1]
                get_arrive+=[arive_counter_data[0]]
        i+=1

    if len(get_arrive)>0:gar = max(get_arrive)
               
    return c, big_equal , gar

def part5(data,rate):
    c= 0
    big_equal=0
    get_arrive=[]
    gar= 0
    i=1
    while i<len(data)-1:
        pre,now,last = data[i-1:i+2]
        if check_reverse(pre , now):
            c+=1
            if last!=1 and rate<=last:
                i+=1
                big_equal+=1
            else:
                arive_counter_data = arive_counter(data,i+1,rate)
                i = arive_counter_data[1]
                get_arrive+=[arive_counter_data[0]]
        i+=1

    if len(get_arrive)>0:gar = max(get_arrive)
               
    return c, big_equal , gar

def part6(data,rate,equal):
    c= 0
    big_equal=0
    get_arrive=[0]
    gar= 0
    keys=list(data.keys())
    i=int(keys[0]+equal)
    counter=0
    big_start=0
    temp_big_start=0
    while i<len(data):
        now,last = [data[x] for x in np.arange(i-equal,i).tolist()] , data[i]
        if all(j < 2 for j in now):
            c+=1
            if last>=rate:
                big_equal+=1
                if counter>0:
                    counter+=1
                    if max(get_arrive) < counter:
                        big_start=temp_big_start
                        
                    get_arrive+=[counter]
                    counter=0
                temp_big_start=0
            else:counter+=1
           
            if counter>0 and temp_big_start==0:
                temp_big_start=i-equal
            i+=(equal+1)
        else:
            i+=1

    if counter!=0:get_arrive+=[counter]
    if len(get_arrive)>0:gar = max(get_arrive)
    return c, big_equal , gar , big_start

def part7(data,rate,equal):
    c= 0
    big_equal=0
    get_arrive=[0]
    gar= 0
    keys=list(data.keys())
    i=int(keys[0]+equal)
    counter=0
    big_start=0
    temp_big_start=0
    while i<len(data):
        now,last = [data[x] for x in np.arange(i-equal,i).tolist()] , data[i]
        if all(j >= 2 for j in now):
            c+=1
            if last>=rate:
                big_equal+=1
                if counter>0:
                    counter+=1
                    if max(get_arrive) < counter:
                        big_start=temp_big_start
                        
                    get_arrive+=[counter]
                    counter=0
                temp_big_start=0
            else:counter+=1
           
            if counter>0 and temp_big_start==0:
                temp_big_start=i-equal
            i+=(equal+1)
        else:
            i+=1

    if counter!=0:get_arrive+=[counter]
    if len(get_arrive)>0:gar = max(get_arrive)
    return c, big_equal , gar , big_start

def extra_data(data):
    counter=0
    less2=[]
    for  i in data:
        if i<2:
            counter+=1
        elif counter>0:
            less2+=[counter]
            counter=0

    more2=[]
    counter=0
    for  i in data:
        if i>=2:
            counter+=1
        elif counter>0:
                more2+=[counter]

                counter=0

    rless2={}
    for i in set(less2):
        rless2.update({i:less2.count(i)})

    rmore2={}
    for i in set(more2):
            rmore2.update({i:more2.count(i)})

    return rless2 , rmore2

def count_special(data):
    res = { 1.97:0,  1.98 :0, 1.99:0 }
    for i in data:
        if i in res.keys():
            res[i]=res[i]+1
    return res

if 1<=order_num<=5:
    res = '\n\n'
    for i,data in enumerate(datas):
        if order_num==1:
            part=part1(data,rate)
        elif order_num==2:
            part=part2(data,rate)
        elif order_num==3:
            part=part3(data,rate)
        elif order_num==4:
            part=part4(data,rate)
        elif order_num==5:
            part=part5(data,rate)
        extra = extra_data(data)
        res+= str(i)+"-   "+'%2s%8s%8s'%(part[0],part[1],part[2])+'\n'

   

if order_num==6:
    res="\n\n"
    data = datas[0]
    less,more = extra_data(data)
    inp = dict(zip(lines,data))
    for i in less:
        p = part6(dict(zip(lines,data)),rate,i)
        res+=str(i)+" = "+str(p[0])+"  "+str(p[1])+"  "+str(p[2])+"  >>"+str(p[3])+"     "
    res+="\n"

if order_num==7:
    res="\n\n"
    data = datas[0]
    less,more = extra_data(data)
    inp = dict(zip(lines,data))
    for i in more:
        p = part7(dict(zip(lines,data)),rate,i)
        res+=str(i)+" = "+str(p[0])+"  "+str(p[1])+"  "+str(p[2])+"  >>"+str(p[3])+"     "
    res+="\n"

if order_num==8:
    res="\n\n"
    for j,data in enumerate(datas):
        res+= str(j)+" - "
        out=count_special(data)
        for i in out:
            res+=str(i)+" = "+str(out[i])+"     "
        res+="\n"

with open("result-"+str(order_num)+".txt","w") as f:
    f.write(res)
