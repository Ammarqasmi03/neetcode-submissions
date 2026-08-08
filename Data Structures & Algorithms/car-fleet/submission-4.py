class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # cars = sorted(zip(position,speed),reverse=True)
        # fleet = 0
        # time = 0

        # for pos , spd in cars:
        #     t = (target-pos)/spd
        #     if t > time:
        #        time = t 
        #        fleet += 1

        # return fleet


        time = [0] * (max(position) + 1)

        for p,s in zip(position,speed):
            time[p] = (target-p)/s

        fleet = [time[-1]]

        for i in range(len(time)-2,-1,-1):
            if fleet and time[i] > fleet[-1]:
                fleet.append(time[i])

        return len(fleet)