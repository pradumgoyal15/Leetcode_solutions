class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        text = str(x)
        return True if text==text[::-1] else False
        