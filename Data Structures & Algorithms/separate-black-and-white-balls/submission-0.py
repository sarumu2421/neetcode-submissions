class Solution:
    def minimumSteps(self, s: str) -> int:
        #want all 0 to the right, and all 1 to the left
        #two pointer

        l = 0 
        steps = 0

        for r in range(len(s)): 
            if s[r] == "0": 
                steps += r - l 
                l += 1

        return steps