class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        for i in range(nums_len-1):
            for j in range(i+1, nums_len):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Beats 29.56% users with Python3
# Need to do it again and optimize it 