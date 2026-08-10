import heapq as h
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            if len(min_heap) < k:
                h.heappush(min_heap,num)
            elif num > min_heap[0]:
                h.heappop(min_heap)
                h.heappush(min_heap,num)

        return min_heap[0]