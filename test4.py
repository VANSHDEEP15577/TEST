r=[]
mul=0
num=int(input("ENTER THE STRING OR NO.:"))
for i in range(0,num):
    w=(input("ENTER:"))
    r.append(w)
print(r)
dele=int(input("ENTER THE NO.:"))
print(r.pop(dele-1))