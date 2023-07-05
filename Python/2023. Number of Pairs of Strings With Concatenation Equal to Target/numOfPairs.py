#Time complexity: O(n)
#Space complexity: O(n)

"""Description:

Given an array of digit strings nums and a digit string
target, return the number of pairs of indices (i, j) (where i != j)
such that the concatenation of nums[i] + nums[j] equals target.

Example 1:
    Input:
        nums = ["777","7","77","77"],
        target = "7777"
    Output: 4

    Explanation: Valid pairs are:
    - (0, 1): "777" + "7"
    - (1, 0): "7" + "777"
    - (2, 3): "77" + "77"
    - (3, 2): "77" + "77"

"""

def is_prefix(str1: str, str2: str) -> bool:
    """Check if str1 is a prefix of str2.

    :param str1: substring to be checked
    :param str2: search string
    :return: true if str1 is a prefix of str2

    """
    return str2.startswith(str1)


class Solution:

    def numOfPairs(self, nums: List[str], target: str) -> int:
        """Implementation of problem solution.

        :param nums: array of digit strings
        :param target: digit string target
        :return: number of pairs of indices (i, j)

        """
        nums_map = {}
        count = 0
        for num in nums:
            if nums_map.get(num):
                nums_map[num] += 1
            else:
                nums_map[num] = 1

        for num in nums:
            if is_prefix(num, target):
                target_suffix = target[len(num):]
                if list_temp := nums_map.get(target_suffix):
                    count += list_temp
                    if target_suffix == num:
                        count -= 1

        return count
