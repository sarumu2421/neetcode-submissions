class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}

        for n in nums: 
            frequencies[n] = frequencies.get(n, 0) + 1

        counts = defaultdict(list)

        for f in frequencies.keys():
            counts[frequencies[f]].append(f) 

        result = [] 
        counter = 0

        for i in range(k): 
            result.append(counts[len(nums) - counter])
            counter += 1

        return result

