# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        answer = head = ListNode(None)      
        l = []
        
        for node in lists:            
            while node:
                print('node: ', node)
                l.append(node.val)
                node = node.next
        
        l.sort()        
        for elem in l:
            new = ListNode(elem)
            head.next = new
            head = head.next
            
        return answer.next
            