class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort = {} 

        for s in strs: 
            st = "".join(sorted(s))
            if st in sort: 
                sort[st].append(s) 
            else: 
                sort[st] = [s] 
            
        return list(sort.values())