import copy
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = []
        l2 = []
        for s in num1:
            l1.append(s)
        for s in num2:
            l2.append(s)

        if len(l1) > len(l2):
            res = copy.deepcopy(l1)
        else:
            res = copy.deepcopy(l2)
        print(res)
        for i in range(min(len(l1), len(l2))):
            n = int(l1[len(l1)-i-1])  + int(l2[len(l2)-i-1])
            res[len(res)-i-1] = str(n)
        res = list(map(int, reversed(res)))
       
        print(res)
        
        for i in range(len(res)):
            if res[i] > 9:
                res[i] -= 10
                if i == len(res) - 1:
                    res.append(1)
                else:
                    res[i+1] += 1
        res = list(map(str, reversed(res)))
        return ''.join(res)  
        

s= Solution()
s1 = "9"
s2 = "99"
print(s.addStrings(s1, s2))