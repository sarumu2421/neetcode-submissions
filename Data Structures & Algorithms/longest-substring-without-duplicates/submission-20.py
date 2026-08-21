class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {} 
        longest = 1 
        curr = 1

        if len(s) == 0: 
            return 0 
        
        if len(s) == 1: 
            return 1

        left = 0
        seen[s[0]] = 0
        right = 1 

        while right < len(s):
            if s[right] not in seen: 
                seen[s[right]] = right
                curr += 1 
                longest = max(curr, longest)  
            else: 
                left = max(left, seen[s[right]] + 1)
                curr = right - left + 1
                seen[s[right]] = right
                longest = max(curr, longest)
            right += 1 
        return longest
            

            




        