class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        cnt = collections.Counter()
        
        for r in range(1, len(s) + 1):
            cnt[s[r-1]] += 1
            common_c = cnt.most_common(1)[0][1]
            
            if r - l - common_c > k:
                cnt[s[l]] -= 1
                l += 1
        
        return r - l
            