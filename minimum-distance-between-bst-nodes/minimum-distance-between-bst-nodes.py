# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:    
        nodes = []

        def check_node(root):
            if root:
                check_node(root.left)
                nodes.append(root.val)
                check_node(root.right)
            return
        
        check_node(root)
        minimum = sys.maxsize
        print(minimum)
        print('nodes: ', nodes)
        for i in range(0, len(nodes) - 1):
            minimum = min(minimum, nodes[i + 1] - nodes[i])
        
        return minimum
        