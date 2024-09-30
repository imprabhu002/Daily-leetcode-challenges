class CustomStack:
    def __init__(self, maxSize: int):
        self.a = []
        self.maxSize = maxSize
    def push(self, x: int) -> None:
        if len(self.a) < self.maxSize:
            self.a.append(x)
    def pop(self) -> int:
        if len(self.a) > 0:
            return self.a.pop()  
        return -1 
    def increment(self, k: int, val: int) -> None:
        rangeloop = min(k, len(self.a))
        for i in range(rangeloop):
            self.a[i] += val
