class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m1 = defaultdict(int)
        m2 = defaultdict(int)

        for c in s:
            m1[c] += 1

        for c in t:
            m2[c] += 1

        return m1 == m2