from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub("[^a-z]", " ", paragraph).split()        
        print('listed: ', paragraph)
        paragraph = Counter(paragraph)
        print('paragrph: ' , paragraph)
        for word in banned:
            del paragraph[word]      

        print('deleted: ' ,paragraph)
        return paragraph.most_common(1)[0][0]
        