class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
        limit = 2 ** 31 - 1 if x > 0 else 2 ** 31
        x *= sign
        res = 0
        while x:
            digit = x % 10
            if res > (limit - digit) // 10:
                return 0
            res = (res * 10) + digit
            x //= 10
        return sign * res