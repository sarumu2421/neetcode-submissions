class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} 

        for s in strs:
            copy = ''.join(sorted(s))
            if copy in anagrams: 
                anagrams[copy].append(s)
            else:
                anagrams[copy] = [s]


        return list(anagrams.values())
        