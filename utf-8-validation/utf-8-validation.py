class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        count = 0
        for n in data:
            if count == 0:
                if n < 0x80:
                    continue
                elif (n & 0xe0) == 0xc0:
                    count = 1
                elif (n & 0xf0) == 0xe0:
                    count = 2
                elif (n & 0xf8) == 0xf0:
                    count = 3
                else:
                    return False
            else:
                if (n & 0xc0) != 0x80:
                    return False
                count -= 1
        
        return count == 0
        
        
                