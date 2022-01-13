n = input()
split =n.split()
limak = int(split[0])
bob = int(split[-1])
years = 0
while True:
    limak*=3
    bob*=2
    years+=1
    if limak>bob:
        break
print(years)

