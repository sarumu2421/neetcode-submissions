class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_nums = set(nums) #so each number is only considered once 

        #dont need to sort thru the nums
        #instead look for "starting" values and count consecutive numbers from there 
        
        best = 0 
        start = 0 
        length = 0

        for num in new_nums: #cannot index over a set using i
            if num - 1 not in new_nums: 
                length += 1
                start = num 
                while start + 1 in new_nums: #we dont need to store the numbers, we just need to count how many consecutive numbers there are remaining
                    start += 1
                    length += 1
                if length > best: 
                    best = length 
        
        return best
            