class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        """
        high = len(strs)
        s = ""
        count = 0
        n = 0
        for i in strs[0]:
            for j in range(1,high):
                if i == strs[j][n]:
                    count += 1
                    continue
                else:
                    break
            if count == high - 1:
                s += i
                n += 1
                count = 0
                continue
            else:
                break
        return s
        """
        v = sorted(list(strs))
        text = ""
        first = v[0]
        last = v[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return text
            text += first[i]
        return text
        

        