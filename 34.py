x=int(input("請輸入一正整數:"))

if x%2==0 and x%11==0 and x%5!=0 and x%7!=0:
    print(x,"為新公倍數?:Yes")
else:
    print(x,"為新公倍數?:No")
