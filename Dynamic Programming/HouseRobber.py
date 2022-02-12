class Solution(object):
    def rob(self, nums):
        def dp(n):
            if n == 0:
                return nums[0]
            elif n == 1:
                return max(nums[0], nums[1])
            else:
                if n not in memo:
                    memo[n] = max(dp(n - 1), dp(n - 2) + nums[n])
                return memo[n]

        memo = {}
        return dp(len(nums) - 1)