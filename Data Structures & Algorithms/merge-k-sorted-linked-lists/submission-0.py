# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        curr = res

        while True:
            minNode = -1

            for i in range(len(lists)):
                if lists[i] is None:
                    continue
                if minNode == -1 or lists[i].val < lists[minNode].val:
                    minNode = i
            
            if minNode == -1:
                break
            
            curr.next = lists[minNode]
            lists[minNode] = lists[minNode].next
            curr = curr.next
        
        return res.next
                