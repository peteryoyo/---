num=list(input("輸入一組四位數字:"))
num2=""
for i in range(4):
    if i==0:
        i+=2
        num3=str((int(num[i])+7)%10)
        num2+=num3
    elif i==1:
        i+=2
        num3=str((int(num[i])+7)%10)
        num2+=num3
    elif i==2:
        i-=2
        num3=str((int(num[i])+7)%10)
        num2+=num3
    else:
        i-=2
        num3=str((int(num[i])+7)%10)
        num2+=num3
print("輸入加密後的數字為:",num2)
