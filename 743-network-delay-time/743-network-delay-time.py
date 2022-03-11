class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = collections.defaultdict(list)
        
        for u, v, w in times:
            g[u].append((v, w))
        
        q = [(0, k)]
        dist = collections.defaultdict(int)
        
        while q:
            time, node = heapq.heappop(q)
            if node not in dist:
                dist[node] = time
                for v, w in g[node]:
                    t = time + w
                    heapq.heappush(q, (t, v))
        
        return max(dist.values()) if len(dist) == n else -1
            
        
