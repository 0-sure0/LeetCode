class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_dist(x, y):
            return sqrt(x ** 2 + y ** 2)
        
        dist = []
        for point in points:
            dist.append((point, get_dist(point[0], point[1])))
        
        dist = list(x[0] for x in sorted(dist, key = lambda x : x[1]))
        
        return dist[:k]
        
        