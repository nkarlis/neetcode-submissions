class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        count = defaultdict(int)
        res = []

        for n in nums:
            count[n] += 1

        for n, cnt in count.items():
            freq[cnt].append(n)

        for i in range(len(freq)-1, 0 , -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            