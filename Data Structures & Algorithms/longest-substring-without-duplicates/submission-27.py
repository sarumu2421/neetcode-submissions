class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  

        if len(s) == 0: 
            return 0 

        if len(s) == 1: 
            return 1
        