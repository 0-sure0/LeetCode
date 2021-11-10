from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewls = list(jewels)
        stones = Counter(stones)  
        answer = 0
        
        for jewl in jewls:
            answer += stones[jewl]
        
        return answer
        
            
        