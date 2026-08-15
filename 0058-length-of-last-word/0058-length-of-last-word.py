class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = s.strip().split(" ")
        return len(lst[-1])