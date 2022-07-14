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
    data= [1.23,2.36,1.17,4.56,1.75,9.98,2.36,5.47,1.11,2.20,2.29,1.68  ]
      
bias=float(input('bias : '))
num=float(input('tedad : '))
reward=float(input('megdar : '))

result = 0
def cond(bias,i):
    if bias >0:
        if i >= abs(bias):return True
        else:return False
    else:
        if i <= abs(bias):return True
        else:return False
active=False
counter = 0
temp_reward = reward
for i in data:
    if not active:
        if cond(bias,i):
            counter+=1
            active=True
            temp_reward = reward
    else:
        if cond(bias,i):
            result+=(bias*temp_reward)-temp_reward
            counter+=1
            if counter>num:
                counter=0
                temp_reward = reward
            else:
                temp_reward =temp_reward/2


        else:
            result -= temp_reward
            active=False
            counter=0
            temp_reward = reward
        
print('profit=',result)
with open('out.txt','w') as f:
    f.write(str(result))