class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        minheap = []

        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(minheap, (dist, x, y))

        for _ in range(k):
            _, x, y = heapq.heappop(minheap)
            res.append([x,y])

        return res