class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.helper(n)
            if n == 1:
                return True
        return False

    def helper(self, n):
        res = 0
        while n:
            digit = n % 10
            n //= 10
            res += digit * digit
        return res
