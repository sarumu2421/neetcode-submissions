class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} 

        for i in range(len(nums)): 
            if (target - num[i]) in hashmap: 
                return [hashmap[target], hashmap[num[i]]] 
            hashmap[num[i]] = i 
        
        