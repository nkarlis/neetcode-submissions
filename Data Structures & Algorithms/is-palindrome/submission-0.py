class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = ""

        for c in s:
            if c.isalnum():
                p+=c.lower()

        l, r = 0, len(p)-1

        while l <r:
            if p[l] == p[r]:
                l+=1
                r-=1
            else:
                return False

        return True