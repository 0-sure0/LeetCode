# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        up = 0
        answer = ListNode()
        cur = answer
        
        num_l1 = ''
        num_l2 = ''
        
        while l1:
            num_l1 += str(l1.val)
            l1 = l1.next
        while l2:
            num_l2 += str(l2.val)
            l2 = l2.next
        
        num_l1 = int(num_l1[::-1])        
        num_l2 = int(num_l2[::-1])
        answer_num = str(num_l1 + num_l2)[::-1]
        
        
        for num in answer_num:           
            cur.next = ListNode(num)
            cur = cur.next
            
        return answer.next        
        