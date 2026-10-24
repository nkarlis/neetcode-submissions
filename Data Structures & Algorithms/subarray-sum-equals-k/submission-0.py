class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Map each prefix sum to how many times it has appeared.
        freq = defaultdict(int)

        # The sum before reading any elements is 0.
        # This lets us count subarrays that start at index 0.
        freq[0] = 1

        prefix, count = 0, 0

        for num in nums:
            # Sum of all elements from the start through this element.
            prefix += num

            # A subarray sums to k when:
            # current prefix - earlier prefix = k
            # So count earlier prefixes equal to prefix - k.
            count += freq[prefix - k]

            # Record this prefix AFTER counting matches, so we don't
            # count an empty subarray when k == 0.
            freq[prefix] += 1

        return count