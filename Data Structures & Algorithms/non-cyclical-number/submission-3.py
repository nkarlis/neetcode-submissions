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
        s = 0
        while n:
            s += (n % 10) ** 2
            n //= 10
        return s

