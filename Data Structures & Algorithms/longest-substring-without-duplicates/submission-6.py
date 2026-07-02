class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charS = set()
        res, l = 0, 0
        for r in range(len(s)):
            while s[r] in charS:
                charS.remove(s[l])
                l += 1
            charS.add(s[r])
            res = max(r - l +1, res)
        return res