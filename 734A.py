n=int(input())
games=input()
a = 0
d = 0
for i in games:
    if "A" in i:
        a += 1
    else:
        d+=1
if a>d:
    print("Anton")
elif a==d:
    print("Friendship") 
else:
    print("Danik")


