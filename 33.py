s=[]
i=0
while i<5:
    c=input("")
    c1=c.split(":")
    s.append(c1)
    i+=1
avg=(int(s[0][1])+int(s[1][1])+int(s[2][1])+int(s[3][1])+int(s[4][1]))/5

print("平均成績為:%.2f" %(avg))
print("最高分科目為:"+ str(max(s)[0]),int(max(s)[1]),"分")
print("最低分科目為:"+ str(min(s)[0]),int(min(s)[1]),"分")

