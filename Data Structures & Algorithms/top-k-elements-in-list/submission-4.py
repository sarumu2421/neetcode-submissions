class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}

        #get frequencies of each number in a hashmap
        for n in nums: 
            frequencies[n] = frequencies.get(n, 0) + 1

        counts = defaultdict(list)

        #now make a new hashmap, grouping the numbers with 
        #the same amount of freqs together
        for f in frequencies.keys():
            counts[frequencies[f]].append(f) 

        result = [] 

        #start with the max number of freq (length of the nums array)
        #and one value at a time from max key descending until 
        #you reach k
        for freq in range(len(nums), 0, -1): 
            for num in counts[freq]: 
                result.append(num)
            if len(result) == k:
                return result


