class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
        x *= sign
        res = 0
        MAX = 2**31
        while x:
            digit = x % 10
            x //= 10
            if res > (MAX - digit)//10:
                return 0
            res = (res * 10) + digit
        return sign * res
            
        