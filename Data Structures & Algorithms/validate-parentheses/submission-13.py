class Solution:
    def isValid(self, s: str) -> bool:

        order = {')': '(', ']':'[', '}':'{'}
        stack = []  

        for i in s: 
            if i in ("{(["): 
                stack.append(i)
            else: 
                if stack and stack.pop() != order[i]: 
                    return False 
                
            
        if not stack: 
            return True 
        else: 
            return False


        