from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        numbers = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        tmp = []

        if len(digits) == 0:
            return answer

        for digit in digits:
            tmp.append(numbers[digit])
        tmp = list(product(*tmp))

        for i in range(len(tmp)):
            answer.append(''.join(tmp[i]))

        return answer
            
            
        
        