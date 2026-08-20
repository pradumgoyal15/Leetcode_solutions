class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        tolerance = 1e-10
        guess = x / 2.0
        while True:
            better_guess = 0.5 * (guess + x / guess)
            if guess - better_guess < tolerance:
                return int(better_guess)
            guess = better_guess
        