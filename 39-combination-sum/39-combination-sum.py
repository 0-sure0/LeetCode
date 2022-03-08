class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates = sorted(candidates)
        
        def dfs(path, s, idx):
            for i in range(idx, len(candidates)):
                if s + candidates[i] < target:
                    dfs(path + [candidates[i]], s + candidates[i], i)
                elif s + candidates[i] == target:
                    ans.append(path + [candidates[i]])
                    return
                else:
                    return

        for idx in range(len(candidates)):
            if candidates[idx] == target:
                ans.append([candidates[idx]])
            else:
                dfs([candidates[idx]], candidates[idx], idx)
                
        return ans