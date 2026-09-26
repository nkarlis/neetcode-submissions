class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        res = 0
        copy = x
        while copy:
            digit = copy % 10
            res = (res * 10) + digit
            copy //= 10
        return res == x