class RandomizedSet:
​
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.map = {}
        
​
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if(val in self.map):
            return False
        self.list.append(val)
        self.map[val] = len(self.list) - 1
        return True
        
​
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if(val not in self.map):
            return False
        index = self.map[val]
        self.list[index] = self.list[-1]
        self.map[self.list[index]] = index
        self.list.pop()
        self.map.pop(val)
        return True
        
​
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.list[random.randint(0, len(self.list)-1)]
        
​
​
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
