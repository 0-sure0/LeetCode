class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common(len(nums))[-1][0]
        