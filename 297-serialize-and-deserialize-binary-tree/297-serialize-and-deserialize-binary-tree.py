# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        
        s = []
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if not node:
                s.append('n')
                continue
            else:
                s.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
            
        return ' '.join(s)
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        
        nodes = data.split()
        root = TreeNode(int(nodes[0]))
        q = collections.deque([root])
        idx = 1
        
        while q:
            node = q.popleft()
            if nodes[idx] != 'n':
                node.left = TreeNode(int(nodes[idx]))
                q.append(node.left)
            idx += 1
            if nodes[idx] != 'n':
                node.right = TreeNode(int(nodes[idx]))
                q.append(node.right)
            idx += 1
        
        return root
            
                
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))