
word=input("輸入一字元為:")
w=[]
for i in range(len(word)):
    w.append(word[i])
b=list(reversed(w))
if w==b:
    print("YES")
else:
    print("NO")

            
    