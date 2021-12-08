class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        for r in range(m):
            idx = bisect.bisect_left(matrix[r], target)            
            if idx < n and idx >= 0:
                if matrix[r][idx] == target:
                    return True
        
        return False
        
                