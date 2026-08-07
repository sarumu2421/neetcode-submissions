class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] 
        results = [0] * len(temperatures)

        for i in range(len(temperatures)): 
            if not stack: 
                stack.append(i) 
            else: 
                while temperature[i] > temperature[stack[-1]]:
                    stack.pop() 
                    results[stack[-1]] = i - stack[-1]
                stack.append(i) 
        
        return results
