# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow contains the middle node
        # we want to reverse the list after the middle node
        prev = None
        curr = slow.next
        # the list after the middle should be separate
        slow.next = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        # 1st list
        first = head
        # 2nd list
        second = prev

        # now merge alternatingly
        while second:
            next1 = first.next
            next2 = second.next

            first.next = second
            second.next = next1

            first =  next1
            second = next2
        
        