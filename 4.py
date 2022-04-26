x=int(input("請輸入x值"))
y=int(input("請輸入y值"))
if x>0 and y>0:
    print("該點位於第一象限，離原點距離為根號",x*x+y*y)
elif x<0 and y>0:
    print("該點位於第二象限，離原點距離為根號",x*x+y*y)
elif x<0 and y<0:
    print("該點位於第三象限，離原點距離為根號",x*x+y*y)
elif x>0 and y<0:
    print("該點位於第四象限，離原點距離為根號",x*x+y*y)
elif x==0 and y==0:
    print("該點位於原點")
elif x==0 and y>0:
    print("該點位於上半平面，離原點距離為根號",x*x+y*y)
elif x==0 and y<0:
    print("該點位於下半平面，離原點距離為根號",x*x+y*y)
elif x>0 and y==0:
    print("該點位於右半平面，離原點距離為根號",x*x+y*y)
else:
    print("該點位於左半平面，離原點距離為根號",x*x+y*y)