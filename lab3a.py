w=0
d=0
u=0
l=0
s=input("enter a sentence:")
r=s.split()
w=len(r)
for i in s:
    if i.isdigit():
        d=d+1
    elif i.isupper():
        u=u+1
    else:
        l=l+1
print("number of words:",w)
print("number of digits:",d)
print("number of uppercase:",u)
print("number of lowercase:",l)