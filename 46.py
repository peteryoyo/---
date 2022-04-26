dict1={}
for i in range(0,4):
    x=str(input("請輸入獎牌名稱:"))
    y=int(input("請輸入獎牌數量:"))
    dict1[x]=y
    item1=list(dict1.items())
for key,value in item1:
    print(key,"得到",value,"面")