class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i: i[1])
        prevEnd = intervals[0][1]
        res = 0
        for start, end in intervals[1:]:
            if prevEnd > start:
                res += 1
            else:
                prevEnd = end
        return res
