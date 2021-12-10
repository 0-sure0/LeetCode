class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def bfs(q):
            while q:
                t = q.popleft()

                for c in candidates:
                    new_t = t[:]                
                    if sum(new_t) + c == target:
                        new_t.append(c)
                        new_t = tuple(sorted(new_t))
                        result[new_t] = 1                       
                    elif sum(new_t) + c < target:
                        new_t.append(c)
                        q.append(new_t)
                    else:
                        continue
            
        result = {}
        for c in candidates:
            if c == target:
                result[tuple([c])] = 1
                continue
            else:
                q = collections.deque([[c]])
                bfs(q)
        
        return list(map(list, result.keys()))