class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stk = []
        
        for i, cur in enumerate(temperatures):
            while stk and cur > temperatures[stk[-1]]:
                last = stk.pop()
                answer[last] = i - last
            stk.append(i)
        
                
        return answer
                
    