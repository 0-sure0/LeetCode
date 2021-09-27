class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target-num], i]
            
            nums_map[num] = i
        
        '''
        answer = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if target == nums[i] + nums[j]:
                    answer.append(i)
                    answer.append(j)
                    return answer '''
        
