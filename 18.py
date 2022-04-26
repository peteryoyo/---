s=[]
for i in range(0,5):
    x=input("")
    if x=="A":
        s.append(1)
    elif x=="J":
        s.append(11)
    elif x=="Q":
        s.append(12)
    elif x=="K":
        s.append(13)
    else:
        s.append(x)
total=int(s[0])+int(s[1])+int(s[2])+int(s[3])+int(s[4])
print(total)
        