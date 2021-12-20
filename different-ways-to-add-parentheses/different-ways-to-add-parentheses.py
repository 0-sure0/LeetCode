class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        return [a+b if c == '+' else a-b if c == '-' else a*b
            for i, c in enumerate(expression) if c in '+-*'
            for a in self.diffWaysToCompute(expression[:i])
            for b in self.diffWaysToCompute(expression[i+1:])] or [int(expression)]
  
        