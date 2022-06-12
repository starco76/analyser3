import numpy as np

with open("d.txt","r") as f:
    d = f.read()
# d='110011100111001110011100011001110001100011001'
pat = input("pattern :")

sep = [int(i[0]) for i in d.split(pat) if len(i)>0]
rr = np.unique(sep,return_counts=True)
res = str(d.count(pat))+ "  ::  "

t1,t0 =0,0
m1,m0 = 0 ,0
for i in range(len(rr[0])):
    res+=str(rr[0][i])+"  =  "+str(rr[1][i])+"      "
for i in sep:
    if i==1:
        t1+=1
        t0=0
    else:
        t0+=1
        t1=0
    if t1>m1:m1=t1
    if t0>m0:m0=t0

res+=f"max loss 1 ={m1}      "
res+=f"max loss 0 ={m0}      "

with open("out.txt","w") as f:
    d = f.write(res)