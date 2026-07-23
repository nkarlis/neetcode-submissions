class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            prevEnd = res[-1][1]
            if prevEnd >= intervals[i][0]:
                res[-1][1] = max(prevEnd, intervals[i][1])
            else:
                res.append(intervals[i])
        return res