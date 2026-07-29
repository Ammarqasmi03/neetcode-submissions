class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        Hashmap = dict()

        for index,element in enumerate(nums):
            diff = target - element

            if diff in Hashmap:
                return [Hashmap[diff],index]

            Hashmap[element] = index
        