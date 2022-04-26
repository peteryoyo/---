s=["飢餓遊戲3","解憂雜貨店","怪獸與他們的產地","哈利波特6","我的阿富汗筆友","祈念之樹","樓下的房客","小王子"]
s1=["房思琪的初戀樂園","等一個人的咖啡","鬼滅之刃14","神農嘗百草","麥田捕手","老人與海","傲慢與偏見","與神同行"]
book=input("請輸入欲租借的書籍:")
if book=="飢餓遊戲3" or book=="解憂雜貨店" or book=="怪獸與他們的產地" or  book=="哈利波特6" or book=="我的阿富汗筆友" or book=="祈念之樹" or book=="樓下的房客" or book=="小王子":
    print("在書架A的第",int(s.index(book))+1,"本")
elif book=="房思琪的初戀樂園" or book=="等一個人的咖啡" or book=="鬼滅之刃14" or  book=="神農嘗百草" or book=="麥田捕手" or book=="老人與海" or book=="傲慢與偏見" or book=="與神同行":
    print("在書架B的第",int(s1.index(book))+1,"本")
else:
    print("查無此書籍")