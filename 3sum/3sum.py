class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            lo, hi = i + 1, len(nums) - 1
            
            while lo < hi:
                sum = nums[lo] + nums[hi] + nums[i]
                                
                if sum < 0:
                    lo += 1
                elif sum > 0:
                    hi -= 1
                else:
                    answer.append([nums[i], nums[lo], nums[hi]])
                    
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
        
        return answer