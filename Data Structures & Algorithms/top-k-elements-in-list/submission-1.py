class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(list) 

        for n in nums: 
            frequencies[n] += 1 

        counts = defaultdict(list)

        for f in frequencies.keys():
            counts[frequencies[f]].append(f) 

        result = [] 
        counter = 0

        for i in range(k): 
            result.append(counts[len(nums) - counter])
            counter += 1

        return result

