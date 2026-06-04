class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            v1 = heapq.heappop(stones)
            v2 = heapq.heappop(stones)

            if abs(v1) == abs(v2):
                continue
            elif abs(v1) > abs(v2):
                v1 -= v2
                heapq.heappush(stones, v1)
            else:
                v2 -= v1
                heapq.heappush(stones, v2)

        stones.append(0)
        return -stones[0]
