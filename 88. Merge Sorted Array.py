class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        for i in range(m, m+n):
            nums1[i] = nums2[j]
            j += 1

        nums1.sort()
# Beats 89.04% of users with Python3
# Need to revise it