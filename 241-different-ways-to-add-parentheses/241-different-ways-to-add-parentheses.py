class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left, right, op):
            t = []
            for l in left:
                for r in right:
                    t.append(eval(str(l) + op + str(r)))
            
            return t
        
        if expression.isdigit():
            return [int(expression)]

        ans = []
        for i, v in enumerate(expression):
            if v in '-+*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                ans.extend(compute(left, right, v))
        return ans