from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for point in points:
            x = point[0]
            y = point[1]
            dist = sqrt(x*x + y*y)
            heapq.heappush(max_heap, (-dist, point))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        res = []
        while k > 0:
            res.append(heapq.heappop(max_heap)[1])
            k -= 1
        return res