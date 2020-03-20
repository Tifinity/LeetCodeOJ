def compressString( S):
    """
    :type S: str
    :rtype: str
    """
    if len(S) == 0: return ''
    res = ''
    tmp = S[0]
    cnt = 0
    for ch in S:
        if ch != tmp:
            res = res + tmp + str(cnt)
            tmp = ch
            cnt = 1
        else:
            cnt += 1 
    res = res + tmp + str(cnt)
    if len(res) > len(S):
        return S
    return res

print(compressString("aabcccccaaabbb"))
print(compressString("abbccd"))
