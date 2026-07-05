class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = [intervals[0]]
        for i in range(1, len(intervals)):
            prevEnd = output[-1][1]
            if prevEnd >= intervals[i][0]:
                output[-1][1] = max(prevEnd, intervals[i][1])
            else:
                prevEnd = intervals[i][1]
                output.append(intervals[i])
        return output