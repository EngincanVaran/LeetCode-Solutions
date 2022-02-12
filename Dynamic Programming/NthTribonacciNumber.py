class Solution(object):
    def tribonacci(self, n):
        def dp(n):
            if n == 0:
                return memo[n]
            if n <= 2:
                return memo[n]
            else:
                if n not in memo:
                    memo[n] = dp(n - 1) + dp(n - 2) + dp(n - 3)
            return memo[n]

        memo = {0: 0, 1: 1, 2: 1}
        return dp(n)