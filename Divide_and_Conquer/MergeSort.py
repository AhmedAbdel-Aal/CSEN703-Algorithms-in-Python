



def mergeSort(a):
    if(len(a)>1) :
        mid = len(a)//2
        L = a[:mid]
        R = a[mid:]

        # sent two halves to be sorted
        mergeSort(L)
        mergeSort(R)

        # combine the two sorted halves

        i = j = k = 0
        while i < len(L) and j < len(R):
         if L[i] < R[j] :
             a[k] = L[i]
             i+= 1
         else:
             a[k]=R[j]
             j+=1
         k+= 1

        while i<len(L) :
             a[k]=L[i]
             i+=1
             k+=1
        while j<len(R):
             a[k]=R[j]
             j+=1
             k+=1








def main():
    a = [122,1,12,13,3,46,6,7]
    print(a)
    mergeSort(a)
    print(a)





main ()