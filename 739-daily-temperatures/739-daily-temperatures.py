class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        answer = [0] * len(t)
        stk = []
        
        for i, cur_t in enumerate(t):
            while stk and cur_t > t[stk[-1]]:
                last = stk.pop()
                answer[last] = i - last
            stk.append(i)
            
        return answer