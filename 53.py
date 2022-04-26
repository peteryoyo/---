i=0
s=int(input("輸入筆數n:"))
s4=[]
s6=[]
while i<s:
    s2=input("請輸入姓名:")
    s5=input("請輸入電子郵件")
    s4.append(s2)
    s4.append(s5)
    s6.append(s4)
    i+=1
s3=input("請輸入要查詢的電子郵件:")
for j in range(0,s):
    for g in range(0,2):
        if str(s6[j][g])==s3:
            print(str(s6[j][g])+"電子郵件為"+str(s6[j][g+1]))
            break   