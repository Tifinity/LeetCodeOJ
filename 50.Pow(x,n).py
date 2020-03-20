class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            x = 1/x
            n = -n
        return self.fast_pow(x, n)

    def fast_pow(self, x, y):
        if y==0:
            return 1
        if y%2==0:
            return self.fast_pow(x*x, y/2)
        if y%2!=0:  
            return self.fast_pow(x*x, int(y/2)) * x
        return 0

s = Solution
a = s.myPow(2, 10)
print(a)