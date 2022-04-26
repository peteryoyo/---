x=float(input("請輸入路程公里數(km):"))
y=75+((x-1.5)//0.25)*5
z=(x-1.5)%0.25
if x<1.5:
    print("所需車資為:75")
else:
    if z==0:
        print("所需車資為",int(y))
    else:
        print("所需車資為",int(y+5))