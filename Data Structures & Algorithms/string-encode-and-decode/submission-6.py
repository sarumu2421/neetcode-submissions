class Solution:

    def encode(self, strs: List[str]) -> str:
        new = [] 
        for s in strs: 
            new.append(f"{len(s)}#{s}")
        
        return "".join(new)


    def decode(self, s: str) -> List[str]:
        left = 0 
        arr = []
        for i in range(len(s)): 
            if s[i] == "#": 
                length = int(s[left:i])
                start = i+1
                end = i+1+length
                arr.append(s[start:end])
                left = end

        return arr



