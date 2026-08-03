class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_elem = dict()

        for num in nums:
            freq_elem[num] = freq_elem.get(num,0) + 1

        # ascending order
        sorted_elem = sorted(freq_elem,key=freq_elem.get)

        result = []

        for i in range(k):
            result.append(sorted_elem.pop())

        return result

        