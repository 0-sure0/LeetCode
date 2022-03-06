class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i + 1 for i in range(n)]

        if n == k:
            return [nums]

        def dfs(nums, path):
            if len(path) == k:
                res.append(path)
                return

            for i in range(len(nums)):
                dfs(nums[i+1:], path + [nums[i]])

        res = []
        for i in range(n):
            dfs(nums[i+1:], [nums[i]])

        return res