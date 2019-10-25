
def lcs_rec(X,Y):
    if len(X)==0 or len(Y)==0:
        return 0
    if(X[0]==Y[0]):
        return 1 + lcs_rec(X[1:],Y[1:])
    else:
        return  max ( lcs_rec(X[1:],Y) ,lcs_rec(X,Y[1:]) )


def lcs_dp(x,y):
    dp = [[0] * (len(y) + 1) for i in range(len(x) + 1)]
    for i in range(len(x)+1):
        for j in range(len(y)+1):
            if(i==0 or j==0):
                dp[i][j]=0
            elif(x[i-1]==y[j-1]):
                dp[i][j]= 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max ( dp[i-1][j] , dp[i][j-1] )
    return dp[len(x)][len(y)]




def main():
    X = "AGGTAB"
    Y = "GXTXAYB"
    print( "Length of LCS_rec is ", lcs_rec(X, Y) )
    print( "Length of LCS_dp is ", lcs_dp(X, Y) )


main()