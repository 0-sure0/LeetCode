from itertools import combinations

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        
        def dfs(cand_sum, idx, path):
            if cand_sum < 0:
                return
            if cand_sum == 0:
                answer.append(path)
                return
            
            for i in range(idx, len(candidates)):
                dfs(cand_sum - candidates[i], i, path + [candidates[i]])
        
        dfs(target, 0, [])
        return answer
            
            
        