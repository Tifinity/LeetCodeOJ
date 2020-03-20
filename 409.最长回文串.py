def longestPalindrome(s):
    '''
    输入: "abccccdd"
    输出: 7
    解释: 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7
    '''
    # 直接模拟，只能出现一个奇数的字符
    res = 0
    flag = 0
    d = {}
    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d.update({ch:1})

    for k, v in d.items():
        if v % 2 == 0:
            res += v
        else:
            flag = 1
            res += (v - 1)
    if flag == 1:
        res += 1
    return res

print(longestPalindrome("abccccdd"))