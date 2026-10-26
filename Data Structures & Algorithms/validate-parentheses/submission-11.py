class Solution:
    def isValid(self, s: str) -> bool:

        order = {')': '(', ']':'[', '}':'{'}
        stack = []  

        for i in s: 
            if i in ("{(["): 
                stack.append(i)
            else: 
                if stack.pop() != order[i]: 
                    return False 
                
            
        return True


        