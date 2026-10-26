class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i in range(len(nums)):
            hash[nums[i]] = i

        for num in nums: 
            diff = target - num 

            if diff in hash: 
                return ([hash[num], hash[diff]])



