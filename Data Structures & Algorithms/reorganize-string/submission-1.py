class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        sorted_char = sorted(count.keys(), key=lambda x: -count[x])
        n = len(s)
        if count[sorted_char[0]] > (n + 1) // 2:
            return ""
        res = [''] * n
        idx = 0
        for char in sorted_char:
            freq = count[char]
            for _ in range(freq):
                res[idx] = char
                idx += 2
                if idx >= n:
                    idx = 1
        return "".join(res)