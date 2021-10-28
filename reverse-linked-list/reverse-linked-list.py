# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = None
        
        if head is None:
            return answer
        
        while head:
            answer, answer.next, head = head, answer, head.next        
        
        return answer