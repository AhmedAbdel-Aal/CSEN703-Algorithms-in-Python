# Problem statment
# Given an array of integers, find its inversion count. The inversion count the number of
# misplaced elements in the array. For example: {2,4,1,3,5} has an inversion count of 3.
# As 1 should be before 2, and 4 should be after 1, and 3 should be before 4

def CountInversions(a,low,high):
    if(len(a)>1):
        mid = len(a)//2
        count=0

        L = a[:mid]
        R = a[mid:]

        k1 = CountInversions(L,low,mid)
        k2 = CountInversions(R,mid,high)
        k3 = combine(a,L,R)

        return count + k1+k2+k3
    else :
        return 0


def combine(a,L,R):
    # the function will apply merge sort on L,R in a temp array  and get number of inversions
    i=j=k=count=0
    temp  = [0]*(len(L)+len(R))
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            temp[k] = L[i]
            i += 1
        else:
            count +=len(L)-i   # if element in right is less than element in left, then its also less than all
                               # all remaining elements in left.
            temp[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        temp[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        temp[k] = R[j]
        j += 1
        k += 1

    for idx in range(len(temp)):
        a[idx] = temp[idx]

    return count

def main():
    a= [1, 20, 6, 4, 55,45,12,11,0]
    i = CountInversions(a,0,len(a)-1)
    print("the array",a," has %d inversion"%i)


main()