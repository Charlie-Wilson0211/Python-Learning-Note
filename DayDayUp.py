#DayDayUp
#dayfactor=0.005
#dayup=pow(1+dayfactor,365)
#daydown=pow(1-dayfactor,365)
#print("dayup is {:.5f},daydown is {:.5f}".format(dayup,daydown))


#dayup=1.0
#dayfactor=0.01
#for i in range(365):
#   if i % 7 in [6,0]:
#        dayup*=(1-dayfactor)
#    else:
#        dayup*=(1+dayfactor)
#print("dayup is {:.5f}".format(dayup))


def dayup(dayfactor):
    dayup=1.0
    for i in range(365):
        if i % 7 in [6,0]:
            dayup*=(1-dayfactor)
        else:
            dayup*=(1+dayfactor)
    return dayup

dayfactor=0.01
while dayup(dayfactor) < pow(1.01,365):
    dayfactor+=0.0001
print("{:.4f}".format(dayfactor))

