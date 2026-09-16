class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        res = 0
        copy = x
        while copy:
            res = (res * 10) + copy % 10
            copy //= 10
        return res == x