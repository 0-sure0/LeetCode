from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub("[^a-z]", " ", paragraph).split()                
        paragraph = Counter(paragraph)
        
        for word in banned:
            del paragraph[word]      

            
        '''
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        counts = Counter(words)        
        return counts.most_common(1)[0][0]
        '''
        
        return paragraph.most_common(1)[0][0]
        
