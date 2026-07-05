class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        r = 0
        cur = 0
        while r < k:
            if blocks[r] == 'W':
                cur += 1
            r += 1
        res = cur
        while r < len(blocks):
            if blocks[r] == 'W':
                cur += 1
            if blocks[l] == 'W':
                cur -= 1
            res = min(res, cur)
            r += 1
            l += 1
        return res
            