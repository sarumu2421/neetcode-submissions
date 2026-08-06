class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter 

        counts = Counter(nums)
        result = []

        for i in range(k): 
            max_key = max(counts, key=counts.get)
            result.append(max_key)
            del(counts[max_key]) 

        return result
            

        
