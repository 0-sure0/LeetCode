class Solution:    
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        checked = [[0] * n for _ in range(m)]

        def _check_islands(r, c):
            islands = 0
            dx = [-1, 0, 1, 0]
            dy = [0, 1, 0, -1]

            for i in range(4):
                y = r + dy[i]
                x = c + dx[i]
                if y >= 0 and y < m and x >= 0 and x < n and checked[y][x] == 0:
                    checked[y][x] = 1
                    if grid[y][x] == '1':
                        _check_islands(y, x)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and checked[r][c] == 0:
                    checked[r][c] = 1
                    _check_islands(r, c)
                    ans += 1    


        return ans
            
                    
                
            
                
        
                    
        