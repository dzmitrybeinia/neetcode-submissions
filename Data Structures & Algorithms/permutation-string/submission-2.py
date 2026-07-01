class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        r = 0
        while r < len(s1):
            freq1[s1[r]] += 1
            freq2[s2[r]] += 1
            r += 1
        l = 0
        while r < len(s2):
            if freq1 == freq2:
                return True
            freq2[s2[r]] += 1
            freq2[s2[l]] -= 1
            if freq2[s2[l]] == 0:
                del freq2[s2[l]]
            l += 1
            r += 1
        return freq1 == freq2
