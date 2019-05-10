class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            return 1 / self.myPowRecur(x, -n)
        return self.myPowRecur(x, n)
        
    def myPowRecur(self, x, n):
        # Base case.
        if n == 0:
            return 1
        
        if n % 2 == 0:
            return self.myPowRecur(x * x, int(n / 2))
        # else:
        return x * self.myPowRecur(x * x, int(n / 2))
