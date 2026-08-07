class Solution:

    def encode(self, strs: List[str]) -> str:
        new_string = "" 
        for s in strs: 
            new_string += str(len(s)) + "$" + s  

        return new_string

    def decode(self, s: str) -> List[str]:
        new_list = []  

        while start < len(s): 
            end = start
            while end != "$": 
                end += 1 
            end += 1
            read_length = int(s[start:end]) #change string number into actual number
            new_list.append(s[end+1:end+read_length]) #adds string that comes after $ 
            start = end + read_length + 1 #reset start to next number 

        return new_list
