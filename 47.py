i=0
s=int(input("輸入筆數n:"))
s4=[]
while i<s:
    s2=input("")
    s1=s2.split(" ")
    s4.append(s1)
    i+=1
for j in range(0,s):
        print (str(s4[j][0])+"牌得到",int(s4[j][1]),"面")


   