class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        count = Counter(nums)
        x = max(count.values())
        for i in count.keys():
            if count[i] == x:
                return i