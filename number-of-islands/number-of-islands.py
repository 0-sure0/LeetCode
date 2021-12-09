class Solution:
     def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def is_island(row, col):
            dr = [-1, 0, 1, 0]
            dc = [0, 1, 0, -1]

            for i in range(4):
                x = col + dc[i]
                y = row + dr[i]
                if 0 <= y <= m - 1 and 0 <= x <= n - 1 and grid[y][x] == '1':
                    grid[y][x] = '0'
                    is_island(y, x)
            return

        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    grid[r][c] = '0'
                    is_island(r, c)
                    ans += 1
        return ans