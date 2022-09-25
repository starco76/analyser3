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
    data= []
    lines = list(range(len(data)))
import numpy as np
mabna=float(input('mabna : '))
bias=float(input('bias : '))
num=int(input('tedad : '))
# reward=float(input('megdar : '))

counter , max_len , next_arrived =0,0,0
next_seq_arrived,next_id=0,0
sid=0
rsid = 0
temp = 1
i=0
end = len(data)-num-1
while i < end:
    item = data[i]
    nx = np.array(data[int(i+1):int(i+1+num)])
    nxt = data[int(i+1+num)]
    if len(nx[nx>=bias])==num and item<mabna:
        if nxt>=mabna:
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
                
        i+=num+1
        counter+=1
        continue
    i+=1


print(counter , next_arrived, max_len ,rsid ,next_seq_arrived,next_id)       
# print('profit=',result)
with open('out2.txt','w') as f:
    f.write(f'{counter=} {next_arrived=}  {max_len=}    id={rsid}   next max len={next_seq_arrived}     next id={next_id}')