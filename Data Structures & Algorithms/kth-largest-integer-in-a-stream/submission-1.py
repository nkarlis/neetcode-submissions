class KthLargest:

    # n logn
    def __init__(self, k: int, nums: List[int]):
        # add and pop in O(logn), min on O(1)
        self.minheap = nums
        self.k = k
        # logn
        heapq.heapify(self.minheap)
        # n times worst
        while len(self.minheap) > self.k:
            # pop the min val
            heapq.heappop(self.minheap)

    # m logn
    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        # don't pop from the heap if elements in heap are less than the size of queu
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        
        # min value is alwayes stored at 0/ root
        return self.minheap[0]
        
