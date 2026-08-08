class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position,speed),reverse=True)
        fleet = 0
        time = 0

        for pos , spd in cars:
            t = (target-pos)/spd
            if t > time:
               time = t 
               fleet += 1

        return fleet
