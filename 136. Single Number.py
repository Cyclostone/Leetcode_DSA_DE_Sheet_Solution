class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_map = {}
        for num in nums:
            if num not in nums_map.keys():
                nums_map[num] = 1
            else:
                nums_map[num] += 1
        for num in nums_map.keys():
            if nums_map[num] == 1:
                return num