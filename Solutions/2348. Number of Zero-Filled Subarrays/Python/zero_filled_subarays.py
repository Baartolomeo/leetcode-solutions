# Time complexity: O(n)
# Space complexity: O(n)

"""Description:

Given an integer array nums, return the number of subarrays filled with 0.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
    Input:
        nums = [1,3,0,0,2,0,0,4]
    Output: 6

    Explanation:
    There are 4 occurrences of [0] as a subarray.
    There are 2 occurrences of [0,0] as a subarray.
    There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.

"""

class Solution:

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """Implementation of problem solution.

        :param nums: integer array
        :return: number of subbarays filled with 0

        """
        zeros = 0
        mem = {-1: 0,
               0: 0,
               1: 1}
        result = 0
        for num in nums:
            if num == 0:
                zeros += 1
                mem[zeros] = zeros + mem[zeros - 1]
            else:
                result += mem[zeros]
                zeros = 0
        else:
            result += mem[zeros]

        return result
