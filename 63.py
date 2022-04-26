from re import I


sum=0
x=int(input("請輸入正整數"))
for i in range(1,x+1):
    if x!=i:
        if x%i==0:
            sum+=i
if sum==x:
    print("perfect")
elif sum>x:
    print("abundant")
else:
    print("dcficient")