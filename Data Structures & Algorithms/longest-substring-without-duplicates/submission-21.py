class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest = 0

        left = 0
        right = 0

        while right < len(s):

            if s[right] in seen:
                left = max(left, seen[s[right]] + 1)

            seen[s[right]] = right

            curr = right - left + 1
            longest = max(longest, curr)

            right += 1

        return longest
            

            

            




        