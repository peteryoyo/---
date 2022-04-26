day=str(input("月跟日為:"))
day1=day.split(" ")
g=""
z=""
g+=day1[0]
z+=day1[1]
if int(g)==1:
    if int(z)>=22:
        print("水瓶座")
    else:
        print("魔羯座")

elif int(g)==2:
    if int(z)>=22:
        print("雙魚座")
    else:
        print("水瓶座")

elif int(g)==3:
    if int(z)>=22:
        print("白羊座")
    else:
        print("雙魚座")

elif int(g)==4:
    if int(z)>=22:
        print("金牛座")
    else:
        print("白羊座")

elif int(g)==5:
    if int(z)>=22:
        print("雙子座")
    else:
        print("金牛座")

elif int(g)==6:
    if int(z)>=22:
        print("巨蟹座")
    else:
        print("雙子座")

elif int(g)==7:
    if int(z)>=22:
        print("獅子座")
    else:
        print("巨蟹座")

elif int(g)==8:
    if int(z)>=22:
        print("處女座")
    else:
        print("獅子座")
elif int(g)==9:
    if int(z)>=22:
        print("天秤座")
    else:
        print("處女座")

elif int(g)==10:
    if int(z)>=22:
        print("天蠍座")
    else:
        print("天秤座")

elif int(g)==11:
    if int(z)>=22:
        print("射手座")
    else:
        print("天蠍座")

elif int(g)==12:
    if int(z)>=22:
        print("魔羯座")
    else:
        print("射手座")

