# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = ListNode()
        second.next = head

        while n > 0:
            first = first.next
            n -= 1
        
        while first:
            first = first.next
            second = second.next
        
        if second.next == head:
            return head.next

        second.next = second.next.next
        return head

        