class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]                    # only one house: rob it
        dp[1] = max(nums[0], nums[1])      # two houses: rob the bigger one

        for i in range(2, len(nums)):
            rob = nums[i] + dp[i - 2]      # rob this house + best from 2 back
            skip = dp[i - 1]               # skip this house, keep best so far
            dp[i] = max(rob, skip)

        return dp[len(nums) - 1]
        