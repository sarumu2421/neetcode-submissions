class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        output = []
        left = 0 
        right = k

        while right <= len(nums): 
            output.append(max(nums[left:right])) 
            left += 1 
            right += 1

        return output
        