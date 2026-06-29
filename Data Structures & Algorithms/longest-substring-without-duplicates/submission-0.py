class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicates = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(s)):
            duplicates[s[r]] += 1
            while duplicates[s[r]] > 1:
                duplicates[s[l]] -= 1
                if duplicates[s[l]] == 0:
                    del duplicates[s[l]]
                l += 1
            res = max(res, r - l + 1)
        return res