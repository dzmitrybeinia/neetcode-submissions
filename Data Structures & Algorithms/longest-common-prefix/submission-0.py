class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            common = strs[0][i]
            for s in strs:
                if i == len(s) or common != s[i]:
                    return res
            res += common
        return res