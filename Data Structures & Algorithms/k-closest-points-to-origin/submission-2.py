import heapq as h
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            distance = point[0]**2 + point[1]**2
            if len(heap) < k:
                h.heappush(heap,(-distance,tuple(point)))
            elif distance < -heap[0][0]:
                h.heappop(heap)
                h.heappush(heap,(-distance,tuple(point)))

        return [list(point) for _,point in heap]

        