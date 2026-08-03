class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxStoreWater = 0

        left = 0
        right = len(heights)-1

        while left <= right:
            width = right - left
            maxStoreWater  = max(maxStoreWater,width * min(heights[left],heights[right]))

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxStoreWater




        