class Solution(object):
    def countCharacters(self, words, chars):
        """
        Counter统计字符个数，for else判断是否可以拼出单词
        时间复杂度O(N)，N为words总长度
        """
        from collections import Counter
        res = 0
        chars_cnt = Counter(chars)
        for word in words:
            word_cnt = Counter(word)
            for ch in word_cnt:
                if chars_cnt[ch] < word_cnt[ch]:
                    break
            else:
                res += len(word)
        return res        