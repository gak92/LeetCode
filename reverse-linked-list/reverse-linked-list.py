# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        temp1 = None
        temp2 = None
        
        while(head):
            temp2 = head.next
            head.next = temp1
            temp1 = head
            head = temp2
            
        return temp1
    
    
    
    
#     1 ->  2 ->  3 ->  4 ->  5
# t1  h    t2