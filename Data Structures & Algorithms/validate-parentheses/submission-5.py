class Solution:
    def isValid(self, s: str) -> bool:
        # stack = [] 

        # for i in s: 
        #     if i == '(' or i == '{' or i == '[': 
        #         stack.append(i) 
            
        #     if i == ')': 
        #         if stack:
        #             if stack[-1] == '(': 
        #                 stack.pop()   
        #             else: 
        #                 return False 
        #         else:
        #             return False
            
        #     if i == '}': 
        #         if stack:
        #             if stack[-1] == '{': 
        #                 stack.pop()   
        #             else: 
        #                 return False
        #         else:
        #             return False

        #     if i == ']': 
        #         if stack:
        #             if stack[-1] == '[': 
        #                 stack.pop()   
        #             else: 
        #                 return False 
        #         else:
        #             return False

        
        # if len(stack) == 0: 
        #     return True 
        # else: 
        #     return False 

        #more efficient way 
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()

        return not stack #returns true is stack is empty

