class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        Hashmap = {}

        for index,element in enumerate(nums):

            if (target - element) in Hashmap:
                return [Hashmap[target - element],index]

            Hashmap[element] = index
        