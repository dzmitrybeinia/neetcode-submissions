class Solution:

    delimeter = "del"

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s
            res += self.delimeter
        return res

    def decode(self, s: str) -> List[str]:
        items = s.split(self.delimeter)
        items.pop()
        return items
