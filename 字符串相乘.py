
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0": return "0"
        l1, l2 = len(num1), len(num2) 
        if l1 < l2: 
            num1, num2 = num2, num1
            l1, l2 = l2, l1
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = "0"
        for i, digit in enumerate(num2):
            tmp = self.multiplyDigit(num1, int(digit)) + "0" * i
            res = self.addStrings(res, tmp)
            print(tmp, res)
        return res

    def multiplyDigit(self, string, n):
        print(string, '!!!', n)
        res = ''
        carry = 0
        for i, char in enumerate(string):
            num = int(char)
            tmp = num * n + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
        return str(carry) + res if carry else res
    
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res

s= Solution()
s1 = "123"
s2 = "456"
print(s.multiply(s1, s2))