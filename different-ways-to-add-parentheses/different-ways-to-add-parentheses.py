class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left, right, op):
            ans = []
            for l in left:
                for r in right:
                    ans.append(eval(str(l) + op + str(r)))
            
            return ans
        
        if expression.isdigit():
            print(expression)
            return [int(expression)]
        
        ans = []
        for idx, v in enumerate(expression):
            if v in '+-*':
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(expression[idx + 1:])
                
                ans.extend(compute(left, right, v))
        return ans
  
        