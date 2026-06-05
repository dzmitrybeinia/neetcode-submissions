class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        groups = {}
        for s in strs:
            s_hash = tuple(sorted(s))
            if s_hash not in groups:
                first = []
                first.append(s)
                groups[s_hash] = first
            else:
                hashes = groups[s_hash]
                hashes.append(s)
                groups[s_hash] = hashes
        return list(groups.values())
        