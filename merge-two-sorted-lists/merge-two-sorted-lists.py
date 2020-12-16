# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        head = dummy
​
        while(l1 != None and l2 != None):
            if (l1.val <= l2.val):
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
​
            dummy = dummy.next
​
        dummy.next = l1 if l1 != None else l2
        return head.next
