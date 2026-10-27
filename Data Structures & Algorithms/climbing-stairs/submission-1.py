class Solution:
    def climbStairs(self, n: int) -> int:
        #backwards fibonacci 

        one = 1 #second to last
        two = 1 #last 

        for i in range(n-1): 
            temp = one
            one = one + two 
            two = temp

        return one





