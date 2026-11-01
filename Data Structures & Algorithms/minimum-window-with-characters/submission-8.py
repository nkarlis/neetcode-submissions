class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = defaultdict(int)
        for c in t:
            countT[c] += 1
        window = defaultdict(int)
        resLen, res = float("inf"), [-1, -1]
        have, need = 0, len(countT)
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if countT[s[r]] == window[s[r]]:
                have += 1
                while have == need:
                    if resLen > r - l + 1:
                        resLen =  r - l + 1
                        res = [l, r]
                    window[s[l]] -= 1
                    if window[s[l]] < countT[s[l]]:
                        have -= 1
                    l += 1
        l, r = res
        return s[l : l + resLen] if resLen != float("inf") else ""

