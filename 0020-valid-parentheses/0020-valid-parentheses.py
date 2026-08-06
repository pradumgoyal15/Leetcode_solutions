class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check = []
        comp = ["(", "[", "{"]
        for paran in s:
            if paran in comp:
                check.append(paran)
            else:
                if len(check) == 0:
                    return False
                elif (paran==")" and check[-1]=="(") or (paran=="]" and check[-1]=="[") or (paran=="}" and check[-1]=="{"):
                    check.pop()
                else:
                    return False
        if len(check) == 0:
            return True
        else:
            return False