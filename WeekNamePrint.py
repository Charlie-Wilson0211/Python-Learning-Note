#WeekNamePrint.py
#WeekStr="星期一星期二星期三星期四星期五星期六星期日"
#WeekId=eval(input("请输入数字(1-7):"))
#if WeekId in range(7):
#    pos=(WeekId-1)*3
#    print(WeekStr[pos:pos+3])
#else:
#    print("error")


WeekStr="一二三四五六日"
WeekId=eval(input("请输入数字(1-7):"))
if WeekId in range(7):
    print("星期"+WeekStr[WeekId-1])
else:
    print("error")
