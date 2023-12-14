# Time complexity: O(k) - k => number of black cells
# Space complexity: O(m*n)

"""Description:

You are given two integers m and n representing the dimensions of a 0-indexed m x n grid.
You are also given a 0-indexed 2D integer matrix coordinates, where coordinates[i] = [x, y] indicates
that the cell with coordinates [x, y] is colored black.
All cells in the grid that do not appear in coordinates are white. A block is defined as a 2 x 2 submatrix of the grid.
More formally, a block with cell [x, y] as its top-left corner where 0 <= x < m - 1 and 0 <= y < n - 1 contains
the coordinates [x, y], [x + 1, y], [x, y + 1], and [x + 1, y + 1].

Return a 0-indexed integer array arr of size 5 such that arr[i] is
the number of blocks that contains exactly i black cells.

Example 1:
    Input: m = 3, n = 3, coordinates = [[0,0]]
    Output: [3, 1, 0, 0, 0]
    Explanation: The grid looks like this:

    There is only 1 block with one black cell, and it is the block starting with cell [0,0].
    The other 3 blocks start with cells [0,1], [1,0] and [1,1]. They all have zero black cells.
    Thus, we return [3, 1, 0, 0, 0].

"""


class Solution:
    def countBlackBlocks(self, m, n, coordinates):
        """Implementation of problem solution.

            :param m: number of rows in matrix
            :param n: number of columns in matrix
            :param coordinates: array of black cells coordinates (x, y)
            :return: array of size 5 such that arr[i] is
                     the number of blocks that contains exactly i black cells
        """
        blocks = {}
        results = [(m - 1) * (n - 1), 0, 0, 0, 0]
        for coordinate in coordinates:
            x, y = coordinate
            for i in range(x - 1, x + 1):
                for j in range(y - 1, y + 1):
                    if i < 0 or j < 0 or i >= m - 1 or j >= n - 1:
                        continue
                    index = i + (m - 1) * j
                    black_cells = blocks.get(index) or 0
                    if results[black_cells] != 0:
                        results[black_cells] -= 1
                    black_cells += 1
                    blocks[index] = black_cells
                    results[black_cells] += 1

        return results
