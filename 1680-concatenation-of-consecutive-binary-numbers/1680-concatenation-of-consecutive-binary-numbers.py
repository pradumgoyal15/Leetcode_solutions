class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        string = ""
        for i in range(1,n + 1):
            string += (str(bin(i)))[2:]
        amt = int(string, 2)
        result = amt % (10**9 + 7)
        return result
        