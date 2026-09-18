class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        MAX, MIN = 2 ** 31, 2**31-1
        if x < 0:
            sign = -1
        x *= sign
        res = 0
        while x:
            digit = x % 10
            if res > (MAX - digit) // 10:
                return 0
            res = (res * 10) + digit
            x //= 10
        return res * sign
            
