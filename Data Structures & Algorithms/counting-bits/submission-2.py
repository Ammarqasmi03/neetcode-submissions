class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = []

        # for i in range(n+1):
        #     mask = i
        #     count = 0
        #     while mask > 0:
        #         if mask & 1:
        #             count += 1
        #         mask >>= 1

        for i in range(n+1):
            num = i
            count = 0
            while num:
                count += num & 1
                num >>= 1

            lst.append(count)

        return lst
        

            
        