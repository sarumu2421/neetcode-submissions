class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0): 
            return 0
            
        longest = 1 
        count = 1

        arr = set(nums)
        arr = sorted(arr)

        for i in range(1,len(arr)): 
            if (arr[i-1] == arr[i]-1):
                count+=1 
            else: 
                longest = max(longest, count)
                count = 1

        longest = max(longest, count)
        return longest
        