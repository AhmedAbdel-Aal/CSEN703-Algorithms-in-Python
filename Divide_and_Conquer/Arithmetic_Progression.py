# Given an array that represents elements of arithmetic progression in order. One element is
# missing in the progression, find the missing number using divide and conquer.


def findMissing(a):
    d = (a[-1]-a[0]) // (len(a))
    mid = len(a)//2

    if(a[mid+1]-a[mid]!=d):
        return a[mid]+d
    elif(a[mid]-a[mid-1]!=d):
        return a[mid]-d

    if(a[mid] == a[0]+mid*d):
        return findMissing(a[mid:])
    else:
        return findMissing(a[:mid])



def main():
    a=[2,4,6,8,10,12,16,20]
    i  =findMissing(a)
    print("we found %d is missing" %i)





main()