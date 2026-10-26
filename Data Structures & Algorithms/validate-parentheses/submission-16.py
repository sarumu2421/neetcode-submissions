class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 == 1: 
            return False

        order = {')': '(', ']':'[', '}':'{'}
        stack = []  

        for i in s: 
            if i in ("{(["): 
                stack.append(i)
            else: 
                if stack and stack.pop() != order[i]: 
                    return False  
                
        return not stack


        