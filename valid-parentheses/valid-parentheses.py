class Solution:
    def isValid(self, s: str) -> bool:       
        stk = []
        
        for p in s:
            if p == '(' or p == '{' or p == '[':
                stk.append(p)                
            elif p == ')':
                if not stk or stk.pop() != '(':
                    return False
            elif p == '}':
                if not stk or stk.pop() != '{':
                    return False
            elif p == ']':
                if not stk or stk.pop() != '[':
                    return False
        
        if stk:
            return False
        
        return True
