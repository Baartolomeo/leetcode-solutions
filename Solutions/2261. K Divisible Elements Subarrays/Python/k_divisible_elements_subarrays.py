#Time complexity: O(n^2)
#Space complexity: O(n^2)

"""Description:

Given an integer array nums and two integers k and p, return
the number of distinct subarrays which have at most k elements divisible by p.

Two arrays nums1 and nums2 are said to be distinct if:

They are of different lengths, or
There exists at least one index i where nums1[i] != nums2[i].
A subarray is defined as a non-empty contiguous sequence of elements in an array.

Example 1:
    Input:
        nums = [2,3,3,2,2],
        k = 2,
        p = 2
    Output: 11

    Explanation:
    The elements at indices 0, 3, and 4 are divisible by p = 2.
    The 11 distinct subarrays which have at most k = 2 elements divisible by 2 are:
    [2], [2,3], [2,3,3], [2,3,3,2], [3], [3,3], [3,3,2], [3,3,2,2], [3,2], [3,2,2], and [2,2].
    Note that the subarrays [2] and [3] occur more than once in nums, but they should each be counted only once.
    The subarray [2,3,3,2,2] should not be counted because it has 3 elements that are divisible by 2.

"""


class Solution:

    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        """Implementation of problem solution.

        :param nums: integer array nums
        :param k: number of maximum elements
        :param p: divisible element
        :return: number of distinct subarrays
        """
        my_dict = {}
        num_str = ''
        divisible = 0
        for i in range(len(nums)):
            divisible = 0
            num_str = ''
            for j in range(i, len(nums)):
                if not (nums[j] % p):
                    divisible += 1
                    if divisible > k:
                        break
                num_str += str(nums[j])
                num_str += ';'
                if not (my_dict.get(num_str)):
                    my_dict[num_str] = '1'
        return len(my_dict.keys())
