#CalBmi.py
'''height,weight=eval(input("请输入身高/（米）和体重/（公斤）:[逗号隔开]"))
bmi=weight/pow(height,2)
print("BMI数值为：{:.2f}".format(bmi))
who=""
if bmi<18.5:
    who="偏瘦"
elif bmi<25:
    who="正常"
elif bmi<30:
    who="偏胖"
else:
    who="肥胖"
print("BMI指标为：国际'{0}',".format(who),end="")

if bmi<18.5:
    who="偏瘦"
elif bmi<24:
    who="正常"
elif bmi<28:
    who="偏胖"
else:
    who="肥胖"
print("国内'{0}'".format(who))'''


height,weight=eval(input("请输入身高/（米）和体重/（公斤）:[逗号隔开]"))
bmi=weight/pow(height,2)
print("BMI数值为：{:.2f}".format(bmi))
who=""
if bmi<18.5:
    who,nat="偏瘦","偏瘦"
elif bmi<24:
    who,nat="正常","正常"
elif bmi<25:
    who,nat="正常","偏胖"
elif bmi<28:
    who,nat="偏胖","偏胖"
elif bmi<30:
    who,nat="偏胖","肥胖"
else:
    who,nat="肥胖","肥胖"
print("BMI指标为：国际'{}',国内'{}'".format(who,nat))



