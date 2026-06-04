class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap
        stones = [-s for s in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
        
            if abs(first) == abs(second):
                continue
            elif abs(first) > abs(second):
                first -= second
                heapq.heappush(stones, first)
            else:
                second -= first
                heapq.heappush(stones, second)

        stones.append(0)
        # return abs(stones[0])


        return -heapq.heappop(stones)