s=[["123","Tom","DTGD"],["456","Cat","CSIE"],["789","Nana","ASIE"],["321","Lim","DBA"],["654","Won","FDD"]]
x=int(input("輸入查詢學號為:"))
if x==123:
    print("學生資料為:"+str(s[1][0]), str(s[1][1]) , str(s[1][2]))
elif x==456:
    print("學生資料為:"+str(s[1][0]), str(s[1][1]) , str(s[1][2]))
elif x==789:
    print("學生資料為:"+str(s[2][0]), str(s[2][1]) , str(s[2][2]))
elif x==321:
    print("學生資料為:"+str(s[3][0]), str(s[3][1]) , str(s[3][2]))
else:
    print("學生資料為:"+str(s[4][0]), str(s[4][1]) , str(s[4][2]))