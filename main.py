# a = float(input('a = '))
# b = float(input('b = '))
# m1 = float(input('m1 = '))
# n1 = float(input('n1 = '))
# s1 = float(input('s1 = '))
# t1 = float(input('t1 = '))

# c = float(input('c = '))
# d = float(input('d = '))
# m2 = float(input('m2 = '))
# n2 = float(input('n2 = '))
# s2 = float(input('s2 = '))
# t2 = float(input('t2 = '))
a ,b ,m ,n,s,t= 12 , 3,2,20,2,1
data = [2.56,2.36,5.65,2.90,1.11,4.98,1.47,1.87,1.69,4.78,9.36]


iterate= 0
start_type = None
stop = 0
for item in data:
    if stop==1 and item<s:stop-=1
    if stop==0:
        if iterate <=m:
            ta = ta = a / 2**iterate
        else:
            ta = a / 2**m
        iterate+=1

        if start_type==None:start_type=True  if item > b else False
        if start_type:
            if item > b:
                calc = ta * b - ta
                print(calc)
            else:
                iterate = 0
                calc = ta * b - ta
                print(-1*calc)
        else:

            if item > b:
                iterate = 0
                calc = ta * b - ta
                print(calc)
            else:
                stop = t+1
                calc = ta * b - ta
                print(-1*calc)
    else:
        stop-=1
        
input()
