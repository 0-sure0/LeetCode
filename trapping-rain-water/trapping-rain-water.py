class Solution:
     def trap(self, height: List[int]) -> int:
        water = 0
        n = len(height)
        lmax = [0] * n
        rmax = [0] * n
        lmax[0] = height[0]
        rmax[n-1] = height[n-1]
        for i in range(1, n):
            lmax[i] = max(lmax[i-1], height[i])
        for i in range(n-2, -1, -1):
            rmax[i] = max(rmax[i+1], height[i])

        water = 0
        for i in range(n):
            water += min(lmax[i], rmax[i]) - height[i]

        return water
                