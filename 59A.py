s=input()
uppercount=0
lowercount=0
for i in s:
    if i.isupper():
        uppercount+=1
    else:
        lowercount+=1
if uppercount > lowercount:
    print(s.upper())
else:
    print(s.lower())