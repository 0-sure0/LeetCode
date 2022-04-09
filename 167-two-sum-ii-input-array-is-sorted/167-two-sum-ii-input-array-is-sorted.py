class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        
        while l <= r:
            t = numbers[l] + numbers[r]
            mid = (l + r) // 2
            
            if t == target:            
                return [l+1, r+1]
            elif t < target:
                l += 1
            else:
                r -= 1
        
        
            
                
                    
                