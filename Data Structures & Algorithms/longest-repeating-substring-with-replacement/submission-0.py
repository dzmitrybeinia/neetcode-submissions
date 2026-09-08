class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        res = 0
        count = defaultdict(int)
        while r < len(s):
            count[s[r]] += 1
            while (r - l + 1) - self.findMaxFreq(count) > k:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res


    def findMaxFreq(self, count: dict) -> int:
        max_freq = 0
        for v in count.values():
            max_freq = max(max_freq, v)
        return max_freq