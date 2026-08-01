class Solution:
    def climbStairs(self, n: int) -> int:
        # arr = [-1]*n

        # def dfs(i):
        #     if i >= n:
        #         return i == n
        #     if arr[i] != -1:
        #         return arr[i]

        #     arr[i] = dfs(i+1) + dfs(i+2)

        #     return arr[i]

        # return dfs(0)

        # if n == 1:
        #     return 1

        # dp = [0] * (n + 1)

        # dp[1] = 1
        # dp[2] = 2

        # for i in range(3,n+1):
        #     dp[i] = dp[i-1] + dp[i-2]

        # return dp[n]

        one , two = 1,1 

        for i in range(n-1):
            one , two = one+two, one 

        return one

        
        

         