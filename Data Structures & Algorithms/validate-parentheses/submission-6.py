class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 

        valid = {')': '(', ']': '[', '}': '{'}

        for i in s: 
            if i in "({[": 
                stack.append(i) 
            else: 
                if stack.pop() != valid[i]: 
                    return False 
                
        return True

        