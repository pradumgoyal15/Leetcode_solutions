class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = nums[-1]
        j = nums[-2]
        return (i-1)*(j-1)
        