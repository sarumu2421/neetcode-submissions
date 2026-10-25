class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #hashmap to count the occurences of letters 
        count = {}
        longest = 0 
        l = 0 # starting pointer

        #right pointer goes through even possible position in s
        for r in range(len(s)): 
            count[s[r]] = 1 + count.get(s[r], 0)
            
            #check if current window is valid 
            # r - l + 1 is the length of the curr window
            while (r - l + 1) - max(count.values()) > k: 
                count[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1) 

        return longest




         
