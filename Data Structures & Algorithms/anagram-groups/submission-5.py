class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #create a hashmap to store anagrams : strings in og list 
        anagrams = {}

        for i in range(len(strs)):
            key = "".join(sorted(strs[i])) #keeps it as a string instead of a list
            if key in anagrams: 
                anagrams[key].append(strs[i]) 
            else:
                anagrams[key] = strs[i]
    
        #keys : values, gets the values directly as a list
        new_list = list(anagrams.values())
        
        return new_list

