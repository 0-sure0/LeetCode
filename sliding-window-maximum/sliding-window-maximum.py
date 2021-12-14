class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = collections.deque()

        current_max = -sys.maxsize
        for i, num in enumerate(nums):            
            while window and nums[window[-1]] <= num:
                window.pop()
            window.append(i)
            
            if window[0] == i - k:
                window.popleft()
            
            if i >= k - 1:
                result.append(nums[window[0]])
        return result