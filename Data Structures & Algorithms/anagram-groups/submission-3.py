class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #create a hashmap to store anagrams : strings in og list 
        anagrams = {}

        for i in range(len(strs)):
            sorted = sorted(strs[i]) 
            if sorted in anagrams: 
                anagrams[sorted].append(strs[i]) 
            else:
                anagrams[sorted] = strs[i]
    
        #keys : values, gets the values directly as a list
        new_list = list(anagrams.values())
        
        return new_list

