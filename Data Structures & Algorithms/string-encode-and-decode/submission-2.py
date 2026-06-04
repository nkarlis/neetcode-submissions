class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for w in strs:
            res += str(len(w))+ "#" + w
        return res


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            j +=1
            i = j +length
            res.append(s[j:i])
        return res