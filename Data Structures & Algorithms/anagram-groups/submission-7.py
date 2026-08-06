class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for i in strs: 
            sort = "".join(sorted(i))
            if sort in output: 
                output[sort].append(i)
            else: 
                output[sort] = [i] 
        
        return list(output.values())