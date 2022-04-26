degree=int(input("請輸入一個度數(正整數):"))
if degree<=120:
    print("Summer months:",degree*2.1)
    print("Non-Summer months:",degree*2.1)
elif 330>=degree>121:
    print("Summer months:",120*2.1+(degree-120)*3.02)
    print("Non-Summer months:",120*2.1+(degree-120)*2.68)
elif 500>=degree>331:
    print("Summer months:",120*2.1+(330-120)*3.02+(degree-120-210)*4.39)
    print("Non-Summer months:",120*2.1+(330-120)*2.68+(degree-120-210)*3.61)
elif 700>=degree>501:
    print("Summer months:",120*2.1+(330-120)*3.02+(degree-120-210-170)*4.97+(500-330)*4.39)
    print("Non-Summer months:",120*2.1+(330-120)*2.68+(degree-120-210-170)*4.01+(500-330)*3.61)
else:
    print("Summer months:",120*2.1+(330-120)*3.02+(degree-120-210-170-200)*5.63+(500-330)*4.39+(700-500)*4.97)
    print("Non-Summer months:",120*2.1+(330-120)*2.68+(degree-120-210-169-200)*4.50+(500-330)*3.61+(700-500)*4.01)