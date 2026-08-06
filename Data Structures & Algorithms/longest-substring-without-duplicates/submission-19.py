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
        chars = set() 
        max_len = 0


        for right in range(len(s)): 
            while s[right] in chars:  
                chars.remove(s[left]) 
                left += 1
            chars.add(s[right])
            max_len = max (len(chars), max_len)

        return max_len