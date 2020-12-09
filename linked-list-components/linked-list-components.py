# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        ptr = head
        res = 0
        comp_found = False
        
        while(ptr != None):
            
            if (ptr.val in G and not comp_found):   # 3
                print(ptr.val)
                res += 1
                comp_found = True
                #ptr = ptr.next
            
            elif((ptr.val not in G) and comp_found):                   # 2
                print(ptr.val)
                comp_found = False
                #ptr = ptr.next
            ptr = ptr.next
        return res
