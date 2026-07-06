class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        students = defaultdict(list)
        heap = []
        for item in items:
            id = item[0]
            val = item[1]
            heapq.heappush(students[id], -val)
        res = []
        for key,val in students.items():
            id = key
            scores = val
            sum = 0
            k = 5
            while k != 0:
                sum += -heapq.heappop(scores)
                k -= 1
            res.append([id, sum // 5])
        res.sort()
        return res