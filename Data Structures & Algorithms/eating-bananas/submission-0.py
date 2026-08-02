import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed = 1
        maxSpeed = max(piles)
        res = maxSpeed

        while minSpeed <= maxSpeed:
            midSpeed = (maxSpeed + minSpeed)//2

            if self.canEatBananas(piles,h,midSpeed):
                res = midSpeed
                maxSpeed = midSpeed - 1
            else:
                minSpeed = midSpeed + 1

        return res

    def canEatBananas(self,piles,hours,speed):
        total_hours = 0

        for pile in piles:
            total_hours += math.ceil(float(pile)/speed)

        return total_hours <= hours


        