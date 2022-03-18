class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        g = collections.defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        
        leaves = [node for node in g.keys() if len(g[node]) == 1]
        
        while n > 2:
            n -= len(leaves)
            new_l = []
            
            for leaf in leaves:
                neighbor = g[leaf].pop()
                g[neighbor].remove(leaf)
                
                if len(g[neighbor]) == 1:
                    new_l.append(neighbor)
            
            leaves = new_l
        
        return leaves
        