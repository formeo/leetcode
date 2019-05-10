class Solution(object):
    def divide(self, dividend, divisor):
        a,b = dividend, divisor
        sig = (a < 0) == (b < 0)
        a, b, res = abs(a), abs(b), 0
        while a >= b:
            x = 0
            while a >= b << (x + 1): x += 1
            res += 1 << x
            a -= b << x
        return min(res if sig else -res, 2147483647)
