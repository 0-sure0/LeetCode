import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        comp = lambda a,b: 1 if a+b>b+a else -1 if a+b<b+a else 0
      
        nums = sorted(list(map(str,nums)), key = functools.cmp_to_key(comp), reverse =True)
        return str(int(''.join(nums)))
        
        
        