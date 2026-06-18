class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            if first > second:
                heapq.heappush(max_heap, -(first - second))
        return -max_heap[0] if len(max_heap) == 1 else 0