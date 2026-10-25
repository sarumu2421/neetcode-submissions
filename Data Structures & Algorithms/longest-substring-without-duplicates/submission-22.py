class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  

        if len(s) == 0: 
            return 0

        if len(s) == 1: 
            return 1 

        longest = 1
        l = 0 
        r = 1  

        while r < len(s): 
            sub = s[l:r]  
            new = s[r] 

            if new in sub: 
                ind = sub.index(new)
                l += ind + 1
    
            curr_len = len(s[l:r + 1])
            longest = max(longest, curr_len)
            r += 1


        return longest 
        