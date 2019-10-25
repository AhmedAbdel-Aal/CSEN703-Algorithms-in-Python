import timeit

# a good approach to tackle a problem using dp , is first
# to solve it recursivly and then try to dynamic program it


def knapSack_rec(val,wt,W):
    if W==0 or len(wt)==0:
        return 0

    if(wt[0]>W):
        return knapSack_rec(val[1:],wt[1:],W)
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else :
        return max(
             knapSack_rec(val[1:],wt[1:],W-wt[0])+val[0]
              ,
              knapSack_rec(val[1:],wt[1:],W)
        )


def knapSack_DP(val,wt,W):
    DP = [[0 for x in range(W+1)] for x in range(len(val)+1)]

    for i in range (len(val)+1):
        for j in range (W+1):
            if i==0 or j==0:
                DP[i][j]=0
            elif wt[i-1]>W:
                DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = max( DP[i-1][j] , DP[i-1][j-wt[i-1]]+val[i-1])

    return DP[len(val)][W]






def main():
    val = [60,100,120]
    w =[10,20,30]
    W = 50
    print ("knap sack solution recusively = ", knapSack_rec(val,w,W) )

def main2():
    val = [60,100,120,60,100,120,60,100,120,60,100,120,60,100,120]
    w =   [10,20,30,10,20,30,10,20,30,10,20,30,10,20,30]
    W = 250
    print ("knap sack solution dynamically programmed = ", knapSack_DP(val,w,W) )


print(timeit.timeit(main2, number=1)*1000)

print(timeit.timeit(main, number=1)*1000)

