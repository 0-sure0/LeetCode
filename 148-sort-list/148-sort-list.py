# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
            
        l.sort()
        root = dummy = ListNode()
        for v in l:
            node = ListNode(v)
            dummy.next = node
            dummy = dummy.next
        
        return root.next