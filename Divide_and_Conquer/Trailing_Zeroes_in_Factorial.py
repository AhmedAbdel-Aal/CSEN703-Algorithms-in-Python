# to get the number of zeroes in factorial of number we have two methods
# 1- brute force method -> calculate the factorial and count number of zeros
# 2- we count the number of divisions that our number could be divided by the power of 5
# for more info about this method see https://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/



def TrailingZereo(n):
    count=0
    i=5
    while(n/i>=1):
        count+=int(n/i)
        i*=5
    return int(count)


# the problem statment
# Given an integer n, find the number of positive integers whose factorial ends with n
# zeroes using divide and conquer


def FindNumbers(n):
    low = n*4   # a proof why low = n*4 and high = n*5 is attached in file Trailing_Zeroes_in_Factorial_Explain
    high = n*5
    while(low<high):
        mid = (int)((low+high)/2)
        k = TrailingZereo(mid)
        if(k<n):
            low= mid+1
        else:
            high=mid
    # low now is the first number to have n zeroes in its factorial
    answer = 0
    l = []
    while(TrailingZereo(low)==n):
        l.append(low)
        low+=1
        answer+=1         # we can get len(l) in the main function but to show return of more than one value
    return answer , l




def main():
    a = 250
    k , list= FindNumbers(a)
    print("there are %d numbers" % k)
    print("which are  = ",list)
    for i in range (len(list)) :
        print(TrailingZereo(list[i]))



main()