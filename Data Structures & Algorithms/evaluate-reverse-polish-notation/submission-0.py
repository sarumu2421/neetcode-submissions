class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 

        for t in tokens: 
            if t not in "+-*/":
                stack.append(int(t))
            else: 
                t1 = stack.pop() 
                t2 = stack.pop() 

                if t == "+": 
                   stack.append(t1+t2)
                elif t == "*": 
                    stack.append(t1*t2)
                elif t == "-": 
                    stack.append(t1-t2)
                else: 
                    stack.append(t1/t2)

        return stack[-1]
        