# Consider an array of distinct numbers sorted in increasing order.
# The array has been rotated (clockwise) k number of times. Given such an array, find the value of k.


def countRotations(a,low, high):
    mid = (int)(low + (high - low)/2);

    if(a[mid]>a[mid+1]):
        return mid+1
    if(a[mid-1]>a[mid]):
        return mid

    # if the drop is not in middle elements, it has to be in one of the sub array
    # id a[mid] > a[high] then the drop fo sure happens in the right array because
    # the array is sorted and whatever the length of the array the last element will not
    # be greater than the middle one
    if(a[mid]>a[high]):
        countRotations(a,mid+1,high)
    else:
        countRotations(a,low,mid-1)








def main():
    a=[5,6,7,8,1,2,3,4]
    k=countRotations(a,0,len(a)-1)
    print("number of rotations  = ",k)

main()
