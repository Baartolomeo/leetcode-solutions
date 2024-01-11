# Time complexity: O(N)
# Space complexity: O(N^2)

"""
Given an integer numRows, return the first numRows of Pascal's triangle.

Example:
    Input:
        numRows = 5
    Output:
        [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1 for i in range(j)] for j in range(1, numRows + 1)]
        if numRows > 2:
            for i in range(2, numRows):
                k = 0
                for j in range(1, len(dp[i]) - 1):
                    dp[i][j] = dp[i - 1][k] + dp[i - 1][k + 1]
                    k += 1
        return dp
