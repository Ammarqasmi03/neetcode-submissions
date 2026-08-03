class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxStoreWater = 0

        left = 0
        right = len(heights)-1

        while left <= right:
            length = (right-left)

            if heights[left] < heights[right]:
                maxStoreWater  = max(maxStoreWater,length * heights[left])
                left += 1
            elif heights[left] > heights[right]:
                maxStoreWater  = max(maxStoreWater,length * heights[right])
                right -= 1
            else:
                maxStoreWater  = max(maxStoreWater,length * heights[left])
                right -= 1
                left += 1

        return maxStoreWater




        