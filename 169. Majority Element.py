class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_map = {}
        nums_len = len(nums)
        for num in nums:
            if num not in num_map:
                num_map[num] = 1
            else:
                num_map[num] += 1
        for i in num_map.keys():
            if num_map[i] > nums_len/2:
                return i
# Beats 28.86% of users with Python3
# Need to do it again and optimize it