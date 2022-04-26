while True:
    x=int(input("輸入第一行的整數為"))
    y=str(input("輸入第二行中數列中的數字為"))
    z=y.split(" ")
    z.sort()
    g=""
    n=0
    if  x!=len(z) or x<int(z[-1]):
        continue
    else:
        for i in range(0,len(z)):
            g+=str(z.count(z[i]))
            n+=int(z.count(z[i]))
        if n==x:
            print("每個數字都有出現過1次")
        else:
            s=list(g)
            s.sort()
            a=int(s[-1])
            for i in range(0,len(z)):
                if a==int(z.count(z[i])):
                    c=int(z[i])
            print(c,"數字有重複出現",a,"次")