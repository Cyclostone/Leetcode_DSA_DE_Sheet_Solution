class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        def reverse_list(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l+1, r-1
        
        reverse_list(0, len(nums)-1)
        reverse_list(0, k-1)
        reverse_list(k, len(nums)-1)
# Beats 52.51% of users with Python3
# Needs to revise and optimise it 