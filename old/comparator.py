fn1 = input("file 1 Name:")
fn2 = input("file 2 Name:")

with open(fn1,"r") as f:
    d1 = f.read()
with open(fn2,"r") as f:
    d2 = f.read()

d1 = d1.split("\n")[0].split(",")
d2 = d2.split("\n")[0].split(",")

same = set(d1)&set(d2)
nsame=",".join(set(d2+d1)-same)
same = ",".join(same)

with open("same.txt","w") as f:
    f.write(same)

with open("not_same.txt","w") as f:
    f.write(nsame)

