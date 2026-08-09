class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left = 0
        # right = len(nums) - 1

        # while left < right:
        #     mid = (left+right)//2
        #     if nums[mid] > nums[right]:
        #         left = mid + 1
        #     else:
        #         right = mid

        # pivot = left
        # left = 0
        # right = len(nums) - 1

        # if target >= nums[pivot] and target <= nums[right]:
        #     left = pivot
        # else:
        #     right = pivot - 1

        # while left <= right:
        #     mid = (left+right)//2

        #     if nums[mid] < target:
        #         left = mid + 1
        #     elif nums[mid] > target:
        #         right = mid - 1
        #     else:
        #         return mid 

        # return -1

        l,r = 0,len(nums)-1  
        res = -1

        while l <= r:
            m = (l+r)//2

            if nums[m] == target:
                res = m
                break

            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return res
        
            



        