money=str(input("輸入月租費及通話時間:"))
money1=money.split(",")
if int(money1[0])==186:
    if int(money1[1])//int(money1[0])>2:
        print("通話費為:%.0f" %(int(money1[1])*0.09*0.8))
    else:
        print("通話費為:%.0f" %(int(money1[1])*0.09*0.9))
elif int(money1[0])==386:
    if int(money1[1])//int(money1[0])>2:
        print("通話費為:%.0f" %(int(money1[1])*0.08*0.7))
    else:
        print("通話費為:%.0f" %(int(money1[1])*0.08*0.8))
elif int(money1[0])==586:
    if int(money1[1])//int(money1[0])>2:
        print("通話費為:%.0f" %(int(money1[1])*0.07*0.6))
    else:
        print("通話費為:%.0f" %(int(money1[1])*0.07*0.7))
elif int(money1[0])==986:
    if int(money1[1])//int(money1[0])>2:
        print("通話費為:%.0f" %(int(money1[1])*0.06*0.5))
    else:
        print("通話費:%.0f" %(int(money1[1])*0.06*0.6))


