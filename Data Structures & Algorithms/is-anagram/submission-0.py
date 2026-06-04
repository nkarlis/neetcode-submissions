class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        numMap1 = {}
        numMap2 = {}

        for s1 in s:
            numMap1[s1]= numMap1.get(s1,0)+1

        for t1 in t:
            numMap2[t1]= numMap2.get(t1,0)+1


        return numMap1 == numMap2