class Solution:
    def maxTransactions(self, transactions: List[int]) -> int:
        balance = 0
        res = 0
        for tr in transactions:
            if tr >= 0 or balance + tr >= 0:
                balance += tr
                res += 1
            elif balance - tr < 0:
                continue
        return res