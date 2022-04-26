M=int(input("請輸入階乘值M:"))
n=1
total=1
while True:
    if total<M:
        n+=1
        total*=n
    else:
        print("超過M為",M,"的最小接乘N值為:",n)
        break
        
    