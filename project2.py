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
    
import numpy as np
bias=float(input('bias : '))
num=int(input('tedad : '))
# reward=float(input('megdar : '))

counter , max_len , next_arrived =0,0,0
sid=0
rsid = 0
temp = 1
i=0
end = len(data)-num-1
while i < end:
    item = data[i]
    nx = np.array(data[int(i+1):int(i+1+num)])
    nxt = data[int(i+1+num)]

    if len(nx[nx>=bias])==num and item<2:
        if nxt>=2:
            next_arrived+=1
            if temp>max_len:
                max_len=temp
                rsid=sid
                sid=0
            temp=1
        else:
            if temp==1:sid=lines[i]
            temp+=1
                
        i+=num+1
        counter+=1
        continue
    i+=1


print(counter , next_arrived, max_len )       
# print('profit=',result)
with open('out2.txt','w') as f:
    f.write(f'{counter=} {next_arrived=}  {max_len=}')