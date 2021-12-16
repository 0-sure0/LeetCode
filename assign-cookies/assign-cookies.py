class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0

        l, r = 0, 0
        while True:
            if l > len(g) - 1 or r > len(s) - 1:
                break
            if g[l] <= s[r]:
                ans += 1
                r += 1
                l += 1
            else:
                r += 1

        return ans
