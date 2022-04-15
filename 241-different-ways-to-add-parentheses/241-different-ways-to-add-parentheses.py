class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        return [a+b if v == '+' else a-b if v == '-' else a*b 
                for i, v in enumerate(expression) if v in '+-*'
                    for a in self.diffWaysToCompute(expression[:i])
                    for b in self.diffWaysToCompute(expression[i+1:])] or [int(expression)]
                    
            