class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s))+"#"+s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            l = i
            while s[l] != "#":
                l += 1
            length = int(s[i:l])
            i = l + 1
            strs.append(s[i:i+length])
            i +=length

        return strs
