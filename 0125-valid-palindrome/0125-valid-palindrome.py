class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for a in s:
            if a.isalnum():
                string += a.lower()
        if string == string[::-1]:
            return True
        else:
            return False