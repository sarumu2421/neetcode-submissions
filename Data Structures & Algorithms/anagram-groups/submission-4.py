class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #create a hashmap to store anagrams : strings in og list 
        anagrams = {}

        for i in range(len(strs)):
            sort = sorted(strs[i]) 
            if sort in anagrams: 
                anagrams[sort].append(strs[i]) 
            else:
                anagrams[sort] = strs[i]
    
        #keys : values, gets the values directly as a list
        new_list = list(anagrams.values())
        
        return new_list

