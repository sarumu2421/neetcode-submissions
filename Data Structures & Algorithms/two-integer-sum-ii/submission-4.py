class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #using 2 pointer method 
        #calulate sums of left and right, if equal to target, return 
        #increment left right based on if sum greater or less than target 

        left_pointer = 0 #1 indexed 
        right_pointer = len(numbers)-1  
        result = []

        while left_pointer < right_pointer: 
            sum = numbers[left_pointer] + numbers[right_pointer]  
            if sum == target: 
                result.append(left_pointer + 1) #1 indexed 
                result.append(right_pointer + 1) 
            elif sum < target: 
                left_pointer += 1 
            else: #sum>target 
                right_pointer += 1 
            
        return result 