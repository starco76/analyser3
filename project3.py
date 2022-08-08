import os
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
    data= [1.32,1.54,2.81,4.71,1.67,5.46,1.23,1.39,1.95,3.36,1.81,2.30]
    lines = list(range(len(data)))
import numpy as np
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
    return sum(list(map(lambda x:int(x),list(str(number).replace('.','')))))

while i < end:
    zoj_np = np.array(list(map(sum_digits_string,data[i:i+zoj])))
    fard_np = np.array(list(map(sum_digits_string,data[i:i+zoj])))
    zoj_check = len(np.where(zoj_np%2==0)[0])==zoj
    fard_check = len(np.where(fard_np%2!=0)[0])==fard
    try:
        nxt = data[int(i+1+num)]
    except:nxt=-1
    if zoj_check and fard_check :
        if nxt>=mabna:
            print(nxt)
            next_arrived+=1
            if temp>max_len:
                max_len=temp
                rsid=sid
                sid=0
            temp=1
        else:
            temp2 = 1
            for j in range(i+2+num,len(data)):
                if data[j]>=mabna:
                    if temp2>next_seq_arrived:
                        next_seq_arrived = temp2
                        next_id = lines[i]
                    break

                temp2+=1

            if temp==1:sid=lines[i]
            temp+=1
                
        i+=1
        counter+=1
        continue
    i+=1

pm = f'{counter=} {next_arrived=}  {max_len=}    id={rsid}   next max len={next_seq_arrived}     next id={next_id}'
with open(os.path.basename(__file__)+'.txt','w') as f:
    f.write(pm)