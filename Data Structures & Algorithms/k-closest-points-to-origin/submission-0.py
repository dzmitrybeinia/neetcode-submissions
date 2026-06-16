from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for point in points:
            x = point[0]
            y = point[1]
            dist = sqrt(x*x + y*y)
            heapq.heappush(min_heap, (dist, point))
        res = []
        while k > 0:
            res.append(heapq.heappop(min_heap)[1])
            k -= 1
        return res