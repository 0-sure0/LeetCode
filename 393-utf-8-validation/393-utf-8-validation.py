class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        count = 0

        for n in data:
            if count == 0:
                if n < 0x80:
                    continue
                elif n & 0xE0 == 0xC0:
                    count = 1
                elif n & 0xF0 == 0xE0:
                    count = 2
                elif n & 0xF8 == 0xF0:
                    count = 3
                else:
                    return False
            else:
                if (n & 0xC0) != 0x80:
                    return False
                count -= 1

        return count == 0