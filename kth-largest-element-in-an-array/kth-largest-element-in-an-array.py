class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(collections.Counter(nums).items(), key = lambda x : x[0], reverse = True)
        
        for key, v in nums:
            k -= v
            if k <= 0:
                return key
            
        
        
        
        
        
        