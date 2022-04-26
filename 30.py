ans=list("1234")
qua=list(str(input("請輸入4個數整數:")))
n=0
b=0
for i in ans:
    for j in qua:
        if i==j:
            if ans.index(i)==qua.index(j):
                n+=1
            else:
                b+=1
print(n,"A",b,"B")
