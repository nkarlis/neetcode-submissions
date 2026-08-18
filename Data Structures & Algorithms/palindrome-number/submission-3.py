class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev = 0
        copy = x
        while copy:
            rev = (rev * 10) + (copy % 10)
            copy //= 10
        return rev == x