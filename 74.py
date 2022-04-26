x=["red","blue","red","green"]
n=0
while n<=10:
    y=input("請輸入輸入四個顏色(中間以空白隔間):")
    n+=1
    if n==10 and y!="red blue red green":
        print("挑戰失敗")
        break
    else:
        if y=="red blue red green":
            print("挑戰成功")
        else:
            s=""
            z=y.split(" ")
            for i in range(0,4):
                if x[i]==z[i]:
                    s+="1"
                elif x[i]!=z[i] and x.count(z[i])>0:
                    s+="2"
                else:
                    s+="3"
            print(s)