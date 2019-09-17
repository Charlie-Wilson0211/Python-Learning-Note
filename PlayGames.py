#playGames.py
#coding = utf-8
from random import random
from time import sleep
global MaxAllowRetryNum
MaxAllowRetryNum=3

def printIntro():
    print("这个程序模拟两个选手A和B的某种能力值")
    print("程序运行需要A和B的能力值（以0到1之间的小数表示）")
    print("每位选手的能力值最多允许有3次的错误输入机会")

def getInputs():
    a=getInput_player("A")
    b=getInput_player("B")
    n=getinput_num()
    return a,b,n

def getInput_player(player):
    global MaxAllowRetryNum
    for tryies in range(MaxAllowRetryNum+1):
        prob=input("请输入选手{}的能力值（0-1）：".format(player))
        try:
            prob=float(eval(prob))
            if prob >= 0 or prob <= 1:
                break
            else:
                print("请核对输入信息，还剩余{}次机会".format(MaxAllowRetryNum-tryies))
        except:
            print("请核对输入信息，还剩余{}次机会".format(MaxAllowRetryNum-tryies))
        if tryies == MaxAllowRetryNum:
                for i in range(5):
                    print("\r所有次数已用完，程序将在{}秒后退出".format(5-i), end="")
                    sleep(1)
                print("\n")
                quit()
    return prob

def getinput_num():
    global MaxAllowRetryNum
    for tryies in range(MaxAllowRetryNum+1):
        num=input("请输入比赛轮数:")
        try:
            num=int(eval(num))
            if num > 0:
                break
            else:
                print("请核对输入信息，还剩余{}次机会".format(MaxAllowRetryNum-tryies))
        except:
            print("请核对输入信息，还剩余{}次机会".format(MaxAllowRetryNum-tryies))
        if tryies == MaxAllowRetryNum:
                for i in range(5):
                    print("\r所有次数已用完，程序将在{}秒后退出".format(5-i), end="")
                    sleep(1)
                print("\n")
                quit()
    return num


def printSummary(winsA,winsB):
    n=winsA+winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA,winsA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB,winsB/n))

def simNGames(n,probA,probB):
    winsA,winsB=0,0
    for i in range(n):
        scoreA,scoreB=simOneNGame(probA,probB)
        if scoreA> scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA,winsB

def simOneNGame(probA,probB):
    scoreA,scoreB=0,0
    serving="A"
    while not gameOver(scoreA,scoreB):
        if serving == "A":
            if random()<probA:
                scoreA += 1
            else:
                serving="B"
        else:
            if random()<probB:
                scoreB += 1
            else:
                serving="A"
    return scoreA,scoreB

def gameOver(scoreA,scoreB):
    return scoreA==15 or scoreB ==15


def main():
    printIntro()
    probA,probB,n = getInputs()
    winsA,winsB = simNGames(n,probA,probB)
    printSummary(winsA,winsB)

main()
