def re(url):
    i = 0
    j = len(url) - 1
    while i < j:
        url[i], url[j] = url[j], url[i]
        i += 1
        j -= 1
    i = 0
    j = 0
    while j < len(url):
        if url[j] == '.':
            k = j - 1
            while i < k:
                url[i], url[k] = url[k], url[i]
                i += 1
                k -= 1
            i = j + 1
        j += 1
    return url

print(re(['w','w','w','.','t','i']))
        