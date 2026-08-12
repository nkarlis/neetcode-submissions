class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2 ** 31 - 1
        MIN = - 2 ** 31
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0     
        while x:
            digit = x % 10
            x //= 10
            
            # Check for overflow before updating res
            if res > (MAX - digit) // 10:
                return 0
                
            res = (res * 10) + digit
            
        return res * sign