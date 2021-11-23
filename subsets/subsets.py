from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]
        
        for i in range(1, len(nums)+1):
            answer.extend(list(map(list, combinations(nums, i))))
        
        return answer