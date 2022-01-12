def watermelon(w):
    if w % 2 == 0 and w>2:
        return "YES"
    else:
        return "NO"
a = int(input())
print(watermelon(a))
