# Time complexity: O(N)
# Space complexity: O(N)

"""
Given an integer n, return an array ans of length n + 1 such that
for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example:
    Input: n = 2
    Output: [0,1,1]
    Explanation:
        0 --> 0
        1 --> 1
        2 --> 10
"""


from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0 for i in range(n + 1)]
        j = 0
        for i in range(1, n + 1):
            if 2 ** j < i:
                j += 1
            if 2 ** j > i:
                j -= 1
            m = 2 ** j
            dp[i] = 1 + dp[i - m]

        return dp
