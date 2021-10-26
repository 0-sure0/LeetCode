# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tmp = []
        node = head
        while node.next:
            tmp.append(node.val)
            node = node.next
        tmp.append(node.val)
        
        return tmp == tmp[::-1]