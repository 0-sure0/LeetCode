class MyHashMap:

    def __init__(self):
        self.arr = [None] * 100000

    def put(self, key: int, value: int) -> None:
        self.arr[key % 100000] = value
        return        
        
    def get(self, key: int) -> int:
        if self.arr[key % 100000] == None:
            return -1
        return self.arr[key % 100000]

    def remove(self, key: int) -> None:
        self.arr[key % 100000] = None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)