# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = head = ListNode(None)
        if not lists:
            return root.next
        
        val = []
        for l in lists:
            while l:
                val.append(l.val)
                l = l.next
        
        val.sort()
        
        for v in val:
            node = ListNode(v)
            head.next = node
            head = head.next
        
        return root.next
        
            