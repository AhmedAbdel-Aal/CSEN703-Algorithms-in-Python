

def maxSegmentSum(a):
    if(len(a)==1):
        return a[0]
    mid = len(a)//2
    l =maxSegmentSum(a[:mid])
    r=maxSegmentSum(a[mid:])
    c=maxCrossingSum(a,mid)
    print(l,r,c)
    return max(l,r,c)


def maxCrossingSum(a,mid):
    print(a,mid)
    ls = -2**30 # almost max int
    lr = -2**30 # almost min int

    # get sum from mid to zero elements --> note that we have to go backwards in first loop
    sum=0
    for i in range(mid,0,-1):
        sum = sum + a[i]
        if(sum>ls):
            ls=sum

    sum=0
    for i in range(mid+1,len(a)):
        sum = sum + a[i]
        if(sum>lr):
            lr=sum

    return ls + lr






def main():
    a=[2, -5, 8, -6, 10, -2]
    sum = maxSegmentSum(a)
    print("the max segment sum = ",sum)



main()