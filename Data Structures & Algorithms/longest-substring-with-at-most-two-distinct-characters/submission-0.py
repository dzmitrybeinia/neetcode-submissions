class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l, r = 0, 0
        freq = defaultdict(int)
        res = 0
        while r < len(s):
            freq[s[r]] += 1
            while len(freq) > 2:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res