class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return collections.Counter(bin(x ^ y))['1']
        