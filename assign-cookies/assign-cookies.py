class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        
        for i in s:
            idx = bisect.bisect_right(g, i)
            if idx > ans:
                ans += 1
        
        return ans
        