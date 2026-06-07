class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        res = []
        for n in freq:
            if freq[n] > len(nums) // 3:
                res.append(n)
        return res