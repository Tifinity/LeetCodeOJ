class Solution:
    def longestConsecutive(self, nums):
        # 一个数字他的前一个不在set里他就是某一个序列的起点
        # 以他为起点遍历后面连续的数
        '''
        输入: [100, 4, 200, 1, 3, 2]
        输出: 4
        解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
        '''
        res = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                tmp = num
                cur = 1
                while tmp + 1 in num_set:
                    tmp += 1
                    cur += 1
                res = max(res, cur)
        return res

    def longestConsecutive2(self, nums):
        '''
        哈希表，每次遍历一个数num，看num-1和num+1在不在哈希表中
        更新 一个连续子序列的两端 为当前最长值，中间的数并不关键
        '''
        res = 0
        h = {}
        for num in nums:
            if num in h:
                continue
            elif num-1 in h and num+1 in h:
                l = h[num-1] + 1 + h[num+1]
                h.update({num: l})
                h.update({num - h[num-1]: l})
                h.update({num + h[num+1]: l})
            elif num-1 not in h and num+1 in h:
                l = 1 + h[num+1]
                h.update({num: l})
                h.update({num + h[num+1]: l})
            elif num-1 in h and num+1 not in h:
                l = h[num-1] + 1 
                h.update({num: l})
                h.update({num - h[num-1]: l})
            elif num-1 not in h and num+1 not in h:
                l = 1
                h.update({num: 1})
            res = max(res, l)
            print(h)
        return res

s = Solution()
print(s.longestConsecutive2([0,3,7,2,5,8,4,6,0,1]))