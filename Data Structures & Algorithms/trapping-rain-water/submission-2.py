class Solution:
    def trap(self, height: List[int]) -> int:
        
        # trapWater = 0
        # n = len(height)

        # leftmax = [0] * n
        # rightmax = [0] * n

        # for i in range(1,n):
        #     leftmax[i] = max(leftmax[i-1],height[i-1])
        #     rightmax[n-i-1] = max(rightmax[n-i],height[n-i])


        # for i in range(n):
            
        #     if min(leftmax[i],rightmax[i]) - height[i] > 0:
        #         trapWater += min(leftmax[i],rightmax[i]) - height[i]

            

        # return trapWater

        # efficent solution

        if not height:
            return 0

        left , right = 0 , len(height) - 1

        leftmax , rightmax = height[left] , height[right]

        trapWater = 0

        while left < right:
            if leftmax < rightmax:
                left += 1
                leftmax = max(leftmax, height[left])
                trapWater += leftmax - height[left]
            else:
                right -= 1
                rightmax = max(rightmax, height[right])
                trapWater += rightmax - height[right]

        return trapWater
        