class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        res = prefix = 0
        for num in nums:
            prefix += num
            res += freq[prefix - k]
            freq[prefix] += 1
        return res
