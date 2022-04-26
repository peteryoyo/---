while True:
    x=str(input("檢測的字串(end結束)"))
    if x=="end":
        print("檢測結束")
        break
    else:
        y=str(input("檢測單一字元"))
        print("字元"+y+"出現的次數為:",int(x.count(y)),"次")