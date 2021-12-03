# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    rang = set()
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.rang.add(low)
        self.rang.add(high)
        
#         def dfs(root):
#             if root:
#                 print('root.val: ', root.val)
                
#                 if low < root.val < high:
#                     self.rang.add(root.val)
#                     dfs(root.left)
#                     dfs(root.right)
#                 elif root.val <= low:
#                     dfs(root.right)
#                 elif root.val >= high:
#                     dfs(root.left)
#                 print(self.rang)
#             return
        # dfs(root)
        # print(self.rang)
        # return sum(self.rang)
        def dfs(node: TreeNode):
            if not node:
                return 0

            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)
            
            
            
        
        