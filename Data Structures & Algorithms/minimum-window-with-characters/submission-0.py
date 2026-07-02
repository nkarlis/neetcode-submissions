class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT, window = defaultdict(int), defaultdict(int)
        for c in t:
            countT[c] += 1
        have, need = 0, len(countT)
        l = 0
        res, resLen = [-1, -1], float("inf")
        for r in range(len(s)):
            window[s[r]] += 1
            if window[s[r]] == countT[s[r]]:
                have += 1
            while have == need:
                # update result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("inf") else ""