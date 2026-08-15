class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(nums,index):

            if index == len(nums):
                result.append(nums.copy())
                return 
            
            for i in range(index,len(nums)):
                # Choose
                nums[i] , nums[index] = nums[index], nums[i]
                # Explore
                backtrack(nums,index+1)
                # Undo
                nums[i] , nums[index] = nums[index], nums[i]

        backtrack(nums,0)

        return result

        