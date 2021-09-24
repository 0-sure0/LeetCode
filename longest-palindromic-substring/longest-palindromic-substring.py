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