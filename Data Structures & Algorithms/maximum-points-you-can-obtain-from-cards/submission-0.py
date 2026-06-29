class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)
        l, r = 0, 0
        window = len(cardPoints) - k
        min_sum = float('inf')
        cur_sum = 0
        while r < len(cardPoints):
            cur_sum += cardPoints[r]
            if r - l + 1 == window:
                min_sum = min(min_sum, cur_sum)
                cur_sum -= cardPoints[l]
                l += 1
            r += 1
        return sum(cardPoints) - min_sum