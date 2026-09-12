class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        maxEl, count = nums[0], 0
        for num in nums:
            freq[num] += 1
            if freq[num] > count:
                count = freq[num]
                maxEl = num
        return maxEl