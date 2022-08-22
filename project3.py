import os
from pickle import NEXT_BUFFER
try:
    import mysql.connector

    conn = mysql.connector.connect(user = 'root',
                                host = 'localhost',
                                database = 'game')

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM `tbl_zarib`')
    data = cursor.fetchall()
    lines=[float(i[0]) for i in data]
    data=[float(i[1]) for i in data]
    conn.close()
except:
    data= [1.19,1.35,1.33,1.08,4.41,7.61,2.18,2.68,73.38,1.00,2.20,2.77,1.14,1.35,1.31,1.77,2.98,3.59,9.64,4.01,3.98,2.75,1.02,1.67,3.02,1.25,3.30,4.60,1.29,89.09,1.32,4.57,1.00,1.27,10.97,3.82,3.18,1.59,1.34,27.73,23.98,1.76,1.52,1.56,1.51,2.07,2.96,2.19,13.13,1.44]
    lines = list(range(len(data)))
import numpy as np
mode =int(input('mode : '))
mabna=2#float(input('mabna : '))
zoj=int(input('zoj : '))
fard=int(input('fard : '))
# reward=float(input('megdar : '))
num = zoj+fard
counter , max_len , next_arrived =0,0,0
next_seq_arrived,next_id=0,0
sid=0
rsid = 0
temp = 1
i=0
end = len(data)-1


def sum_digits_string(number):
    if mode==2:
        number = str(number)
        res = number.split('.')
        out = int(res[0])
        if len(res)==2:
            out+=sum(list(map(lambda x:int(x),list(str(res[1])))))
        return out
    elif mode==3:
        number = str(number)
        res = number.split('.')
        out = int(res[0])
        if len(res)==2:
            out+= int(res[1])
        return out
    else:
        return sum(list(map(lambda x:int(x),list(str(number).replace('.','')))))


while i < end:
    # print(data[i])
    zoj_np = np.array(list(map(sum_digits_string,data[i:i+zoj])))
    fard_np = np.array(list(map(sum_digits_string,data[i+zoj:i+num])))
    zoj_check = len(np.where(zoj_np%2==0)[0])==zoj
    fard_check = len(np.where(fard_np%2!=0)[0])==fard
    try:
        nxt = data[int(i+num)]
    except:nxt=-1
    if zoj_check and fard_check :
        # print(data[i:i+zoj],'=>', zoj_np,data[i+zoj:i+num],'=>',fard_np,f'{nxt=}')
        counter+=1
        if nxt>=mabna:
            next_arrived+=1
            if temp>max_len:
                max_len=temp
                rsid=sid
                sid=0
            temp=1
            i=i+num
            continue
        else:
            # print(data[i:i+zoj], zoj_np,data[i+zoj:i+num],fard_np,nxt,'*****')
            temp2 = 1
            for j in range(i+1+num,len(data)):
                if data[j]>=mabna:
                    if temp2>next_seq_arrived:
                        next_seq_arrived = temp2
                        next_id = lines[i]
                    break

                temp2+=1

            if temp==1:sid=lines[i]
            temp+=1
                
        i+=1
        continue
    i+=1

pm = f'tedade kol= {counter}\ntedad resydan be 2= {next_arrived}\nbeshtarin tekrar= {next_seq_arrived}\nid= {next_id}\nbeshtarin tebg olgo= {max_len}\nid={rsid}'
print(pm)
with open(os.path.basename(__file__)+'.txt','w') as f:
    f.write(pm) 