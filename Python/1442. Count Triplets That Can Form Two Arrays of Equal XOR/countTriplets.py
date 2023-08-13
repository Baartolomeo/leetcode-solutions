from typing import List
#Time complexity: O(n^2)
#Space complexity: O(n^2)
"""Description:

Given an array of integers arr.
We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).
Let's define a and b as follows:
a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.
Return the number of triplets (i, j and k) Where a == b.

Example:
    Input: arr = [2,3,1,6,7]
    Output: 4
    Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)

"""


def countTriplets(arr: List[int]) -> int:
    """Implementation of problem solution.

        :param arr: array of integers
        :return: number of triplets (i, j and k) Where a == b.
    """
    xor_a_map = {i: {} for i in range(1, len(arr))}
    for i in range(0, len(arr) - 1):
        xor = arr[i]
        for j in range(i + 1, len(arr)):
            xor ^= arr[j]
            if not xor_a_map[j].get(xor):
                xor_a_map[j][xor] = 1
            else:
                xor_a_map[j][xor] += 1

    result = 0
    for j in range(1, len(arr)):
        xor_b = arr[j]
        dict_xor_a = xor_a_map[j]
        for k in range(j, len(arr)):
            xor_b ^= arr[k]
            if count := dict_xor_a.get(xor_b):
                result += count

    return result
