# Given a non negative array, find the number of subsequences having product smaller
# # than K.

def productSubSeqCount_rec(a,k,sum):
    if(len(a)==0 and sum >k ) or (len(a)==0  and sum==1):
        return 0
    if (len(a)==0 and k>sum):
        return 1
    return productSubSeqCount_rec(a[1:],k,sum*a[0]) + productSubSeqCount_rec(a[1:],k,sum)

def productSubSeqCount_dp(a,k):
    dp = [[0]*(len(a)+1) for i in range(k+1)]

    for i in range (1,k+1):
        for j in range(1,len(a)+1):
            dp[i][j] = dp[i][j-1]

            if(a[j-1]<= i  and  a[j-1]!=0):
                dp[i][j] += dp[i//a[j-1]] [j-1] +1
    print(dp)
    return dp[k][len(a)]

def main():
    A = [ 1,2, 3, 4]
    k = 10
    print(productSubSeqCount_dp(A, k))


main()