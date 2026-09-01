class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False  

        sort = "".join(sorted(s1)) 

        left = 0 
        right = len(s1)

        while right <= len(s2): 
            curr = "".join(sorted(s2[left:right]))
            if sort == curr: 
                return True 
            else: 
                left += 1
                right += 1 

        return False




        