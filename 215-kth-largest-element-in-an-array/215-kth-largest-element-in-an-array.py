class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(Counter(nums).items(), key = lambda x : x[0], reverse = True)
        cnt = 0
        
        for n, c in nums:
            cnt += c
            if cnt >= k:
                return n
            