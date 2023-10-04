
class MyHashMap:

    def __init__(self):
        self.list = [None] * 100

    def put(self, key: int, value: int) -> None:

        if key > len(self.list) -1:
            self.list = self.list + [None]* (10 + key - len(self.list))
        self.list[key] = value

    def get(self, key: int) -> int:
        if key < len(self.list):
            val = self.list[key] 
            if val != None:
                return val
        return -1
        
    def remove(self, key: int) -> None:
        if key < len(self.list):
            self.list[key] = None
