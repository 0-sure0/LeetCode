import re
class Solution:
    def isPalindrome(self, s: str) -> bool:  
        s = re.sub('[^a-zA-Z0-9]', '', s)
        s = s.lower()
        
        if s == s[::-1]:
            return True
        return False
    
    '''
    s = s.lower()
    s = re.sub('[^a-zA-Z0-9]', '', s)
    
    return s == s[::-1]
    '''
