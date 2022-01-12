n = int(input())
for i in range(n):
    ask = input()
    if len(ask) > 10:
        print(ask[0]+ str(len(ask)-2) +ask[-1])
    else:
         print(ask)