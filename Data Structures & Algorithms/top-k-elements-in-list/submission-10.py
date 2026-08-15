class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter 

        counts = Counter(nums) 
        output = []

        buckets = [[] for _ in range(len(nums) + 1)] 

        for num, freq in counts.items(): 
            buckets[freq].append(num)  
        
        count = 0
        
        for freq in range(len(buckets) - 1, 0, -1):
            if len(output) >= k:
                break

            output.extend(buckets[freq])

        return output[:k]

        
