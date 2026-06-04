class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            s1, s2 = abs(heapq.heappop(stones)), abs(heapq.heappop(stones))
            if s1 > s2:
                heapq.heappush(stones, -(s1 - s2))

        return abs(stones[0]) if len(stones) != 0 else 0

