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
        serialized = ['#'] #idx 1 ~ ...
        tree = collections.deque([root])
        while tree:
            node = tree.popleft()            
            if node:
                tree.append(node.left)
                tree.append(node.right)
                
                serialized.append(str(node.val))
            else:
                serialized.append('#')
        return ' '.join(serialized)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '# #':
            return None
        
        nodes = data.split()        
        root = TreeNode(int(nodes[1]))        
        q = collections.deque([root])
        
        idx = 2
        while q:
            node = q.popleft()
            if nodes[idx] is not '#':
                node.left = TreeNode(int(nodes[idx]))
                q.append(node.left)
            idx += 1
            
            if nodes[idx] is not '#':
                node.right = TreeNode(int(nodes[idx]))
                q.append(node.right)
            idx += 1
        return root
            
            
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))