class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return self.valid(l, r - 1, s) or self.valid(l + 1, r, s)
        return True
    
    def valid(self, l: int, r: int, s: str) -> bool:
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True