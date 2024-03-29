#CalPi.py
#pi=0
#N=100
#for k in range(N):
#    pi+=1/pow(16,k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
#print(pi)

#from random import random
#from time import perf_counter
#DARTS =1000000
#hits=0.0
#start=perf_counter()
#for i in range(1,DARTS+1):
#    x,y=random(),random()
#    dist=pow(x**2+y**2,0.5)
#    if dist <=1.0:
#        hits+=1
#pi = 4*(hits/DARTS)
#print("圆周率是：{}".format(pi))
#print("运行时间是：{:.5f}s".format(perf_counter()-start))


from random import random
from time import perf_counter
import turtle

turtle.setup(1000,1000,200,200)
DARTS =10000
hits=0.0
start=perf_counter()
turtle.pensize(5)
for i in range(1,DARTS+1):
    turtle.pencolor("gold")
    turtle.penup()
    x,y=random(),random()
    dist=pow(x**2+y**2,0.5)
    if dist <=1.0:
        hits+=1
        turtle.goto(x*1000-500,y*1000-500)
        turtle.pendown()
        turtle.fd(1)
    else:
        turtle.pencolor("purple")
        turtle.goto(x*1000-500,y*1000-500)
        turtle.pendown()
        turtle.fd(1)

pi = 4*(hits/DARTS)
print("圆周率是：{}".format(pi))
print("运行时间是：{:.5f}s".format(perf_counter()-start))
sleep(10)

