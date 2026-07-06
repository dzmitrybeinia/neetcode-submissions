class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        res = 0
        heap = [n for n in sticks]
        heapq.heapify(heap)
        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            val = first + second
            res += val
            heapq.heappush(heap, val)
        return res