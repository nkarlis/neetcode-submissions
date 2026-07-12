class Solution:
    def longestPalindrome(self, s: str) -> str:
        resL, res = 0, 0

        for i in range(len(s)):
            l, r = i, i
            while l > -1 and r < len(s) and s[r] == s[l]:
                if r - l + 1 > res:
                    res = r - l + 1
                    resL = l
                l -= 1
                r += 1
            l, r = i, i + 1
            while l > -1 and r < len(s) and s[r] == s[l]:
                if r - l + 1 > res:
                    res = r - l + 1
                    resL = l
                l -= 1
                r += 1
        return s[resL : resL + res]
