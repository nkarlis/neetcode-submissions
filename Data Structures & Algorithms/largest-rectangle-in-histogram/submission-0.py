class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []
        # Stores indices of the heights array in a 
        # monotonically increasing order
        # Iterate up to n (inclusive) to handle any 
        #remaining bars in the stack at the end.
        # When i == n, we treat it as a virtual bar 
        # of height 0 to flush out the stack.
        for i in range(n + 1):
        # While the stack is not empty, and either:
        # 1. We reached the end (i == n)
        # 2. The current bar is shorter than or equal to the 
        # bar at the index stored at the top of the stack
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
            # Pop the index of the bar that we are calculating 
            # the area for
                height = heights[stack.pop()]
                # Calculate the width of the rectangle:
                # - If the stack is empty after popping, the popped 
                # bar was the shortest from index 0 up to i-1.
                # - Otherwise, the width is the distance between 
                # the current index i and the new stack top 
                # stack[-1], minus 1.
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea