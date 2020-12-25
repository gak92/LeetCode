        self.temp = self.iter.next() if self.iter.hasNext() else None
        
​
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.temp
        
        
​
    def next(self):
        """
        :rtype: int
        """
        ret = self.temp
        self.temp = self.iter.next() if self.iter.hasNext() else None
        return ret
        
​
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.temp is not None
        
​
# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
