class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force way 
        #max_length = 0

        # for i in range(len(s)): 
        #     length = 0 
        #     chars = set() 
        #     for j in range(i, len(s)):
        #         if s[j] in chars: 
        #             break
        #         else: 
        #             chars.add(s[j])
        #             length += 1 
        #     max_length = max(max_length, length)
        
        # return max_length 

        #optimal way: sliding window 
        #pointers at each end of string, decrease everytime a char is already in the string 

        left = 0 
        right = 1 
        chars = set() 
        chars.add(s[left])

        while left < right: 
            if s[right] not in chars: 
                chars.add(s[right]) 
            else: 
                left += 1
                chars.remove(s[left]) 
            right += 1
            
        return len(chars)