class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        heap = defaultdict(set)
        max_freq = 0
        for num in nums:
            freq[num] += 1
            if freq[num] == 1:
                heap[1].add(num)
            else:
                heap[freq[num] - 1].remove(num)
                heap[freq[num]].add(num)
            max_freq = max(max_freq, freq[num])
        res = []
        while k > 0 and max_freq > 0:
            cur_set = heap[max_freq]
            for n in cur_set:
                res.append(n)
                k -= 1
                if k == 0:
                    return res
            max_freq -= 1
        return res


# [1,2,2,3,3,3]

# k = 2

# 1 = 1
# 2 = 2
# 3 = 3

# 1 = {1}
# 2 = {2}
# 3 = {3}