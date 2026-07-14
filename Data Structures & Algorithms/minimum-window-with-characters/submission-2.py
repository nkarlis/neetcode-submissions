class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT, window  = defaultdict(int), defaultdict(int)
        for c in t:
            countT[c] += 1
        need, have = len(countT), 0
        l = 0
        resLen, res = float("inf"), [-1, -1]
        for r in range(len(s)):
            window[s[r]] += 1
            if window[s[r]] == countT[s[r]]:
                have += 1
            while need == have:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                if window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if res != float("inf") else ""
                
        