class Solution:
    def search(self, nums: List[int], target: int) -> int:        
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
            
        def bin_search(lo, hi):
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return -1
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                break
        
        if nums[i] <= target <= nums[-1]:
            return bin_search(i, len(nums) - 1)
        else:
            return bin_search(0, i-1)
               
        
            