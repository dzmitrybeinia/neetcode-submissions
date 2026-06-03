class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1 = [0] * 26
        t1 = [0] * 26
        for ch in s:
            s1[ord(ch) - ord('a')] += 1
        for ch in t:
            t1[ord(ch) - ord('a')] += 1
        for i in range(len(s1)):
            if s1[i] != t1[i]:
                return False
        return True