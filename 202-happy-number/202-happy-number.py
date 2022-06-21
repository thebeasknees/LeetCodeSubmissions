class Solution:
    def isHappy(self, n: int) -> bool:
        mem = set()
        while n!= 1:
            if n in mem:
                return False
            mem.add(n)
            n = self.sumSquaredDigits(n)
        return True
    
    def sumSquaredDigits(self, n):
        res = 0
        while n != 0:
            res += (n % 10) ** 2
            n //= 10
        return res