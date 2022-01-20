n=input()
words=input()
words=words.lower()
lst=[]
for i in words:
    if i not in lst:
        lst.append(i)
print("YES") if len(lst)==26 else print("NO")