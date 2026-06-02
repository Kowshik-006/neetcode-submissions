# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next
        
        idx = l - n

        if idx == 0:
            return head.next
        
        curr = head
        itr = 0

        while itr < idx - 1:
            curr = curr.next
            itr += 1
        
        curr.next = curr.next.next

        return head