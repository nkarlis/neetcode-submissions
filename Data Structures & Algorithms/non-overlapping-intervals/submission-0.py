class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        prev = intervals[0][1]
        count = 0
        for i in range(1,len(intervals)):
            if prev > intervals[i][0]:
                prev = min(intervals[i][1], prev)
                count+=1
            else:
                prev = intervals[i][1]
        return count