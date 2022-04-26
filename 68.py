ans=list(str(input("請輸入第一組數字:")))
qua=list(str(input("請輸入第二組數字:")))
n=0
b=0
for i in ans:
    for j in qua:
        if i==j:
            if ans.index(i)==qua.index(j):
                n+=1
            else:
                b+=1
if n==4:
    print(n,"A",b,"B全對")
else:
    print(n,"A",b,"B加油")