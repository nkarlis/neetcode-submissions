class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        output = []
        minheap = []

        for x, y in points:
            res = x**2 + y**2
            heapq.heappush(minheap, (res, x, y))


        # heapq.heapify(minheap)

        for _ in range(k):
            _, x, y = heapq.heappop(minheap)
            output.append([x,y])

        return output