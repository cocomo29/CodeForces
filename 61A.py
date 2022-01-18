n = input()
n2 = input()
st = ""
for i in range(len(n)):
    if n[i] != n2[i]:
        st+="1"
    else:
        st+="0"
print(st)