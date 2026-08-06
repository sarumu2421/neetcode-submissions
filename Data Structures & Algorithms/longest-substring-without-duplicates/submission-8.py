class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0

        for i in range(len(s)): 
            length = 0 
            chars = set() 
            for j in range(i, len(s)):
                if s[j] in chars: 
                    break
                else: 
                    chars.add(s[j])
                    length += 1 
            max_length = max(max_length, length)
        
        return max_length