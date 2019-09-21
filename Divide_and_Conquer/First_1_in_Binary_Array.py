


def firstOneUnSorted(a,low,high):
    if(low<high):
        mid = (low + high) // 2
        l=r=-1

        if(a[mid]==1):
            l=firstOneUnSorted(a,low,mid)
            r=mid
        else:
            l=firstOneUnSorted(a,low,mid)
            r=firstOneUnSorted(a,mid+1,high)

        # if both sub arrays has no ones
        if(l==-1 and r==-1):
            return -1
        # if one sub array has 1 ( max(l,r) will choose the not -1 pointer)
        elif(r==-1 or l==-1):
            return max(l,r)
        # if both sub arrays has ones get the first one
        else:
            return l
    else:
        #Conditional Expressions (Python’s Ternary Operator)
        return -1 if (a[low]==0)else low








def firstOneSorted(a):
    low = 0
    high = len(a)
    while(low<=high):
        mid = (low + high) // 2
        if(a[mid]==1 and (mid==0 or a[mid-1]==0) ):
            return mid
        elif(a[mid-1]==1):
            high=mid-1
        else:
            low = mid+1
    return -1




a = [0,0,0,1]
idx = firstOneUnSorted(a,0,len(a)-1)
idx2 = firstOneSorted(a)
print("index of first one  = ",idx)