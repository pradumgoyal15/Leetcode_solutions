class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if "IV" in s:
            s = s.replace("IV", "F")
        if "IX" in s:
            s = s.replace("IX", "N")
        if "XL" in s:
            s = s.replace("XL", "A")
        if "XC" in s:
            s = s.replace("XC", "B")
        if "CD" in s:
            s = s.replace("CD", "O")
        if "CM" in s:
            s = s.replace("CM", "Y")
        
        vals = {"I": "1", "V": "5", "X": "10", "L": "50", "C": "100", "D": "500", "M": "1000", "F": "4", "N": "9", "A": "40", "B": "90", "O": "400", "Y": "900"}
        count = 0
        lst = []
        for i in s:
            lst.append(vals[i])
        for j in lst:
            count += int(j)
        return count


