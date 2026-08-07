class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0 
        chars = set() 

        for i in range(len(s)): 
            for j in range(i, len(s)): 
                if s[j] in chars: 
                    max_length = 0 
                    chars = set() 
                    break
                else: 
                    max_length += 1
        
        return max_length