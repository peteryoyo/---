i=0
s=int(input("輸入筆數n:"))
s4=[]
while i<s:
    s2=input("")
    s1=s2.split(" ")
    s4.append(s1)
    i+=1
s3=input("輸入欲查詢單字:")
for j in range(0,s):
    for g in range(0,2):
        if str(s4[j][g])==s3:
            print(str(s4[j][g])+"中文意思為"+str(s4[j][g+1]))
            break   

