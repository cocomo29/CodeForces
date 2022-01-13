n = input()
lst = []
for i in n:
    if i not in lst:
        lst.append(i)
if len(lst)%2 ==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
    
