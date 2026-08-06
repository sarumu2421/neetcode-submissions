class MinStack:

    def __init__(self):
        self.arr = []
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        min = self.arr[0]
        for c in self.arr: 
            if c < min: 
                min = c
        return min

        
