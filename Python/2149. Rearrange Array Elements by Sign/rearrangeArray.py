#Time complexity: O(n)
#Space complexity: O(n)

"""Description:

You are given a 0-indexed integer array nums of even length
consisting of an equal number of positive and negative integers.

You should rearrange the elements of nums such that
the modified array follows the given conditions:

    * Every consecutive pair of integers have opposite signs.
    * For all integers with the same sign, the order
      in which they were present in nums is preserved.
    * The rearranged array begins with a positive integer.

Return the modified array after rearranging the elements
to satisfy the aforementioned conditions.

"""


class Solution:
  
    def rearrangeArray(self, nums):
      """Implementation of problem solution.

        :param nums: array of integers
        :return: modified array after rearranging the elements
                 to satisfy the aforementioned conditions.
      """
      positive_ints = []
      negative_ints = []
      rearranged_ints = []
      for num in nums:
        if num > 0:
          positive_ints.append(num)
        else:
          negative_ints.append(num)

      for positive, negative in zip(positive_ints, negative_ints):
        rearranged_ints.append(positive)
        rearranged_ints.append(negative)

      return rearranged_ints
