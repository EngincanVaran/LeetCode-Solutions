class Solution(object):
    def minCostClimbingStairs(self, cost):
        length = len(cost)
        def dp(n):
            if n >= length:
                return 0
            else:
                if n not in memo:
                    memo[n] =  cost[n] + min(dp(n+1), dp(n+2))
                return memo[n]
        memo = {}
        return min(dp(0), dp(1))