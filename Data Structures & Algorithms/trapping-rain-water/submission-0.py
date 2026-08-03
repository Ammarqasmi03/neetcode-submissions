class Solution:
    def trap(self, height: List[int]) -> int:

        trapWater = 0
        n = len(height)

        leftmax = [0] * n
        rightmax = [0] * n

        for i in range(1,n):
            leftmax[i] = max(leftmax[i-1],height[i-1])
            rightmax[n-i-1] = max(rightmax[n-i],height[n-i])


        for i in range(n):
            
            if min(leftmax[i],rightmax[i]) - height[i] > 0:
                trapWater += min(leftmax[i],rightmax[i]) - height[i]

            

        return trapWater

        