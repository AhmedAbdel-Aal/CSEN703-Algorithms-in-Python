# Given a string, count number of subsequences of the form ai bj ck
# , i.e., it consists of i ’a’
# characters, followed by j ’b’ characters, followed by k ’c’ characters where i >= 1, j >=1 and k >= 1.


def HowManySequence(s):
    dp=[[0 for i in range(len(s))] for i in range(3)]
    for i in range(2,-1,-1):
        for j in range(len(s)-1,-1,-1):
                if(j==len(s)-1):
                    if(i==2 and s[-1]=='c'):
                      dp[i][j]=1
                    else:
                      dp[i][j]=0
                if(j<len(s)-1):
                    if (i == 0 and s[j] == 'a') or (i == 1 and s[j] == 'b') :
                        dp[i][j] = dp[i+1][j+1] + 2 * dp[i][j + 1]
                    else:
                       dp[i][j]=dp[i][j+1]
    #print(dp)
    return dp[0][0]

def main():
    s = "aaacbbbc"
    k = HowManySequence(s)
    print("there are {0} possible sequences".format(k))

main()
