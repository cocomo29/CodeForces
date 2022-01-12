n = int(input())
count = 0

for i in range(n):
    ask = input()
    if ask.count("1") > 1:
        count+=1    
        
print(count)