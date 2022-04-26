x=input("請輸入A的好友:")
x1=input("請輸入B的好友:")
y=x.split(" ")
y1=x1.split(" ")
sum=0
for i in y:
    for j in y1 :
        if i==j:
            sum+=1
print(sum)
