class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for w in strs:
            s += str(len(w)) + "#" + w

        return s

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            j += 1
            i = j + length

            res.append(s[j:i])
        return res

