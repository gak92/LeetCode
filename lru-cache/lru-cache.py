class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None
​
​
class LRUCache:
​
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
​
    def get(self, key: int) -> int:
        if key in self.map:
            n = self.map[key]                   # get the node
            self._remove(n)                     # remove from cache
            self._add(n)                        # add again to cache
            return n.val
        return -1
        
​
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._remove(self.map[key])
        n = Node(key, value)
        self._add(n)
        self.map[key] = n
        if len(self.map) > self.capacity:               # if capacity increase remove LRU node
            n = self.head.next
            self._remove(n)
            del self.map[n.key]
        
        
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        
        
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.next = self.tail
