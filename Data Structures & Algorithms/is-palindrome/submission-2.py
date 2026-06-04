class Solution:
    def isPalindrome(self, s: str) -> bool:
        norm = ""

        for c in s:
            if c.isalnum():
                norm += c.lower()

        l,r = 0 , len(norm) - 1

        while l<=r:
            if norm[l] == norm[r]:
                l+=1
                r-=1
            else:
                return False
        return True