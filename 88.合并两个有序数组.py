class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # 从后往前双指针，不需要额外空间
        i = m + n - 1
        j = n - 1
        k = m - 1
        while k>=0 and j>=0:
            if nums1[k] < nums2[j]:
                nums1[i] = nums2[j]
                j -= 1
            else:
                nums1[i] =  nums1[k]
                k -= 1
            i -= 1
        nums1[:j + 1] = nums2[:j + 1]