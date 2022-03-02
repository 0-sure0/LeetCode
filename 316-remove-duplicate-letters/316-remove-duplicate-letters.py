class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, checked, stk = collections.Counter(s), set(), []
        
        for char in s:
            counter[char] -= 1
            if char in checked:
                continue
            
            while stk and stk[-1] > char and counter[stk[-1]] > 0:
                checked.remove(stk.pop())
            
            stk.append(char)
            checked.add(char)
        
        return ''.join(stk)            