class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        import heapq 
        stones = list(map(lambda x: -x, stones))
        
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, x - y)

        return -stones[0] if len(stones) else 0

s = Solution()
print(s.lastStoneWeight([2,2]))