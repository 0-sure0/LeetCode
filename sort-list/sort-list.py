# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        l = []
        while head:
            l.append(head.val)
            head = head.next
        
        l.sort()
        root = dummy = ListNode(l[0])
        
        for i in range(1, len(l)):
            node = ListNode(l[i])
            dummy.next = node
            dummy = dummy.next
        
        return root