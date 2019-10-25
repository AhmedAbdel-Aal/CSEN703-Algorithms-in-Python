import math


def EF(n,d):  # n for nomirator , d for dominator
   a=[] # array to hold dominators
   while (n>0):
       x = math.ceil(d/n)
       n = n*x - d
       d = d*x
       a.append(x)
   return a


def main():
    arr = EF(11,12)
    for i in arr :
        print("1/%d +"%i,end=" ")

main()