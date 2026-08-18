class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        maxCount, el = 0, 0
        for n in nums:
            count[n] += 1
            if count[n] > maxCount :
                maxCount = count[n]
                el = n
        return el