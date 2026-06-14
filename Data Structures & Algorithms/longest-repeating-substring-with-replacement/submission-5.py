class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res, maxf = 0, 0, 0
        count = defaultdict(int)
        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(count[s[r]], maxf)

            while  r - l + 1 - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(r-l+1, res)
        return res