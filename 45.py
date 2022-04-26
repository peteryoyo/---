month=int(input(""))
day=int(input(""))
s=(month*2+day)%3
if month<=12:
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12 and day<=31:
        if s==0 :
            print("普通")
        elif s==1:
            print("吉")
        else:
            print("大吉")
    elif month==4 or month==6 or month==11 and day<=30:
        if s==0 :
            print("普通")
        elif s==1:
            print("吉")
        else:
            print("大吉")
    elif month==2 and day<=28:
        if s==0 :
            print("普通")
        elif s==1:
            print("吉")
        else:
            print("大吉")
    else:
        print("已超出範圍")