import heapq as h
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-num for num in stones]
        h.heapify(stones)   

        while len(stones) > 1:
            y = -h.heappop(stones)
            x = -h.heappop(stones)
            
            if y != x:
                h.heappush(stones,-(y-x))

        if len(stones) == 0:
            return 0
        return -stones[0]

            
            
        