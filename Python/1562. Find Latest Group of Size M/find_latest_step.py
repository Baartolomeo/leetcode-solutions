# Time complexity: O(n)
# Space complexity: O(n)

"""Description:

Given an array arr that represents a permutation of numbers from 1 to n.
You have a binary string of size n that initially has all its bits set to zero. At
each step i (assuming both the binary string and arr are 1-indexed) from 1
to n, the bit at position arr[i] is set to 1.
You are also given an integer m. Find the latest step at which there exists a
group of ones of length m. A group of ones is a contiguous substring of 1's
such that it cannot be extended in either direction.
Return the latest step at which there exists a group of ones of length exactly m.
If no such group exists, return -1.

Example:
    Input:
        arr = [3,5,1,2,4],
        m = 1
    Output: 4
    Explanation:
        Step 1: "00100", groups: ["1"]
        Step 2: "00101", groups: ["1", "1"]
        Step 3: "10101", groups: ["1", "1", "1"]
        Step 4: "11101", groups: ["111", "1"]
        Step 5: "11111", groups: ["11111"]
        The latest step at which there exists a group of size 1 is step 4.

"""

class Solution:

    def __init__(self):
        self.arr = []
        self.m = 0

    def check(self, l: int, p: int, i: int) -> int:
        p_res = -1
        l_res = -1
        if l <= p:
            if self.arr[i] >= l and self.arr[i] <= p:
                left = self.arr[i] - l
                right = p - self.arr[i]
                if (left == self.m or right == self.m):
                    return i
                if left > self.m:
                    l_res = self.check(l, self.arr[i] - 1, i - 1)
                if right > self.m:
                    p_res = self.check(self.arr[i] + 1, p, i - 1)
                if l_res or p_res:
                    return p_res if p_res > l_res else l_res
            else:
                l_res = self.check(l, p, i - 1)
                if l_res != -1:
                    return l_res

        return -1

    def findLatestStep(self, arr: List[int], m: int) -> int:
        """Implementation of problem solution.

        :param arr: array that represents a
                    permutation of numbers from 1 to n.
        :param m: length of ones groyp
        :return: latest step which there exists
                 a group of ones
        """
        self.arr = arr
        self.m = m
        if m == len(arr):
            return len(arr)
        res = self.check(1, len(arr), len(arr) - 1)
        return res
