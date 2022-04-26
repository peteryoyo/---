N=str(input("輸入一整數數列"))
N2=N.split(" ")
for i in range(0,len(N2)):
    if int(N2.count(N2[i]))>len(N2)/2:
        a=int(N2[i])
        print("過半元素為:",a)
        break
    else:
        print("過半元素為:NO")
        break
    
