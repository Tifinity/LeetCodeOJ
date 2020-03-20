def add(s1, s2):
    res = ''
    chs = '0123456789abcdefghijklmnopqrstuvwxyz'
    i = len(s1) - 1
    j = len(s2) - 1
    carry = 0
    while i >= 0 or j >= 0:
        num1 = chs.find(s1[i]) if i>=0 else 0
        num2 = chs.find(s2[j]) if j>=0 else 0
        tmp = num1 + num2 + carry 
        carry = tmp // 36 if tmp >= 36 else 0
        res = chs[tmp % 36] + res
        i -= 1
        j -= 1

    return res

a = '1a2z'
b = 'm3'
print(add(a, b))  