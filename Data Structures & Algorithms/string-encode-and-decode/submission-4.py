class Solution:

    delimeter = ";8;"

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s +self.delimeter
        return res

    def decode(self, s: str) -> List[str]:
        return s.split(self.delimeter)[:-1]
