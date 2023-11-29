#Time complexity: O(logn)
#Space complexity: O(1)
"""Description

The complement of an integer is the integer you get
when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer n, return its complement.

Example:
    Input: n = 5
    Output: 2
    Explanation: 5 is "101" in binary, with complement "010"
    in binary, which is 2 in base-10.

"""


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        """Implementation of problem solution.

            :param int: integer to complement
            :return: complement of n
        """
        complement_num = 0
        if n == 0:
            complement_num = 1
        else:
            i = 0
            while (num := 2 ** i) < n:
                if not (n & 1 << i):
                    complement_num += num
                i += 1

        return complement_num
