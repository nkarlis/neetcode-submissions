"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        mp = defaultdict(int)
        for i in range(len(intervals)):
            mp[intervals[i].start] += 1
            mp[intervals[i].end] -= 1
        prev, res = 0, 0
        for i in sorted(mp.keys()):
            prev += mp[i]
            res = max(prev, res)
        return res

        