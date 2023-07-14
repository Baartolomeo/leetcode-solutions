

"""Description:

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer;
in other words, it is the product of some integer with itself.
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example:
    Input: n = 12
    Output: 3
    Explanation: 12 = 4 + 4 + 4.

"""


class Solution:

    def numSquares(self, n: int) -> int:
        """Implementation of problem solution.

        :param n: given integer
        :return: the least number of perfect
                square numbers that sum to n
        """
        nums = []
        i = 1
        while True:
            if (square := i**2) > n:
                break
            nums.append(square)
            i += 1
        dp = [i for i in range(n + 1)]

        for i in range(1, len(nums)):
            for j in range(nums[i], n + 1):
                missing_value = j - (j//nums[i])*nums[i]
                dp[j] = min((j//nums[i]) + dp[missing_value], dp[j])

        return dp[n]