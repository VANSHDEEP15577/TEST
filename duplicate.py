r=[]
num=int(input("ENTER NO:"))
for i in range(0,num):
    e=input("ENTER:")
    r.append(e)
print(r)
f=set(r)
print("THE FINAL LIST IS",list(f))