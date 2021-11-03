# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd, even = head, head.next
        first_even = even
        
        while odd and even and odd.next and even.next:
            odd.next = even.next
            odd_prev = odd            
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = first_even
        return head
        
            