class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        count = Counter(nums)
        for i, j in count.items():
            if j==1:
                return i