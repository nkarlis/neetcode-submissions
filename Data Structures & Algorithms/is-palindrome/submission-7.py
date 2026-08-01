class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        for c in s:
            if c.isalnum():
                temp += c.lower()
        l, r = 0 , len(temp) - 1
        while l < r:
            if temp[l] != temp[r]:
                return False
            l += 1
            r -= 1
        return True