class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        fin = defaultdict(list)
        # key will be sorted s and values would be the real str
        # group by the keys
        for s in strs:
            sortedS = ''.join(sorted(s))
            fin[sortedS].append(s)
        return list(fin.values())

        