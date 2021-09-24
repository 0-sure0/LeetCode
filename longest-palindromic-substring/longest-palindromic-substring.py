class Solution:
    def longestPalindrome(self, s: str) -> str:
        dic = defaultdict(str)

        if s == s[::-1]:
            return s
        for i in range(len(s)):
            for j in range(i, len(s)+1):
                tmp = s[i:j]
                if tmp == tmp[::-1]:
                    dic[tmp] = len(tmp)
        return sorted(dic.items(), key = lambda x: x[1], reverse = True)[0][0]
        '''
        def expand(left: int, right: int) -> str:            
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left+1 : right-1]
        
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        for i in range(len(s) - 1):
            result = max(result, expand(i, i+1), expand(i, i+2), key = len)
            
        return result
        '''
