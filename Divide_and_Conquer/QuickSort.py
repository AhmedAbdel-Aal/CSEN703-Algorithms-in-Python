

def QuickSort(a,start,end):
   if(start<end):
    pivot = a[-1]
    idx = partition(a,start,end)
    # print("pivot idx = ",idx)
    # print("after pivot partition = ",a)
    QuickSort(a,start,idx-1)
    QuickSort(a,idx,end)





def partition(a,l,r):
    pivot = a[r]
    # print("pivot is  = ",pivot)
    # print("to be altered",a[l:r])
    while (l<r):
        while(a[l]<pivot):
                l+=1
        while(a[r]>pivot):
                 r-=1
        if(l<r):
         a[l],a[r]=a[r],a[l]
    return (r)



def main():
    a = [11,1,12,13,3,46,6,7]
    print(a)
    QuickSort(a,0,len(a)-1)
    print(a)



main()