class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT, window = defaultdict(int), defaultdict(int)
        for c in t:
            countT[c] += 1
        l, resLen = 0, float("inf")
        res = [-1, -1]
        have, need = 0, len(countT)
        for r in range(len(s)):
            window[s[r]] += 1
            if window[s[r]] == countT[s[r]]:
                have += 1
            while have == need:
                if resLen > r - l + 1:
                    resLen = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                if window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r+1] if resLen != float("inf") else ""
       


