class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for s in strs:
            key = tuple(sorted(list(s)))
            dic[key].append(s)

        return dic.values()