class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        sub = []
        res = []
        arr.sort()
        for i in range(len(arr)-1):
            sub.append(abs(arr[i+1] - arr[i]))

        min_sub = min(sub)
        for i in range(len(sub)):
            if sub[i] == min_sub:
                res.append([arr[i], arr[i+1]])
        
        return res

    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        res = []
        arr.sort()
        min_dif = arr[1] - arr[0]
        for i in range(0, len(arr)-1):
            tmp = arr[i+1] - arr[i]
            if tmp == min_dif:
                res.append([arr[i], arr[i+1]])
            elif tmp < min_dif:
                min_dif = tmp
                res = [[arr[i], arr[i+1]]]
        return res

s = Solution()
print(s.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))