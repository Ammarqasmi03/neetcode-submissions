class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        HashMap = {}
        
        nums.sort()
        
        for i in range(len(nums)-2):
            left = i+1 
            right = len(nums)-1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    HashMap[nums[i],nums[left],nums[right]] = True
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return [list(triplet) for triplet in HashMap.keys()] 


 