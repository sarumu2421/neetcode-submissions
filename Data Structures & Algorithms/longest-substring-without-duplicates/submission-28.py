class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  

        if len(s) == 0: 
            return 0 

        if len(s) == 1: 
            return 1
        

        seen = set()
        l = 0 
        max_len = 0

        for r in range(len(s)): 

            if s[r] not in seen: 
                seen.add(s[r]) 
            else:  
                while s[r] in seen: 
                    seen.remove(s[l]) 
                    l += 1
                seen.add(s[r]) 

            max_len = max(max_len, r - l + 1)
        
        return max_len


