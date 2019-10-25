# Given an array ‘arr’ containing the weight of ‘N’ distinct items,
# and two knapsacks that can withstand ‘W1’ and ‘W2’ weights,
# the task is to find the sum of the largest subset of the array ‘arr’,
# that can be fit in the two knapsacks.
# Its not allowed to break any items in two, i.e an item should be put in one of the bags as a whole.
#
# Examples:
#
# Input : arr[] = {8, 3, 2}
# W1 = 10, W2 = 3
# Output : 13
# First and third objects go in the first knapsack.
# The second object goes in the second knapsack. Thus, the total weight becomes 13.

def maxWeight(arr, n, w1_r, w2_r, i):
    # Base case
    if i == n:
        return 0
    if dp[i][w1_r][w2_r] != -1: #if this sub-problem has a solution return it
        return dp[i][w1_r][w2_r]

    fill_w1, fill_w2, fill_none = 0, 0, 0

    if w1_r >= arr[i]:
        fill_w1 = arr[i] + maxWeight(arr, n, w1_r - arr[i],
                                     w2_r, i + 1)

    if w2_r >= arr[i]:
        fill_w2 = arr[i] + maxWeight(arr, n, w1_r,
                                     w2_r - arr[i], i + 1)

    fill_none = maxWeight(arr, n, w1_r, w2_r, i + 1)

    dp[i][w1_r][w2_r] = max(fill_none, max(fill_w1,fill_w2))

    return dp[i][w1_r][w2_r]


if __name__ == "__main__":
    # Input array
    arr = [8, 2, 3]
    maxN, maxW = 31, 31
    # 3D array to store  states of DP
    dp = [[[-1] * maxW] * maxW] * maxN
    n = len(arr)
    w1, w2 = 10, 3
    print("max sum of weights = %d"%maxWeight(arr, n, w1, w2, 0))