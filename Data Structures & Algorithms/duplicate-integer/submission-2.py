class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_dup = set(nums)
        if (len(no_dup) != len(nums)): 
            return True 
        else: 
            return False
        