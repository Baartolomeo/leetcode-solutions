# Time complexity:  O(n^2)
# Space complexity: O(n)

"""Description:

Given an integer array nums, return the length of the longest strictly increasing subsequence.

Input:
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output:
    4
Explanation:
    The longest increasing subsequence is [2, 3, 7, 101],
    therefore the length is 4.

"""


class Solution:

    def __init__(self):
        self.dp = None

    def lengthOfLIS(self, nums):
        self.dp = [0 for i in range(len(nums))]
        max_sub = -1
        for i in range(len(nums) - 1, -1, -1):
            len_temp = self.traverse(nums, i, 1)
            if len_temp > max_sub:
                max_sub = len_temp
        return max_sub

    def traverse(self, nums, start_index, act_lis):
        if self.dp[start_index]:
            return self.dp[start_index]
        max_lis = act_lis
        for i in range(start_index, len(nums)):
            temp_lis = act_lis
            if nums[i] > nums[start_index]:
                if self.dp[i]:
                    temp_lis += self.dp[i]
                else:
                    temp_lis = self.traverse(nums, i + 1, act_lis + 1)
                if temp_lis > max_lis:
                    max_lis = temp_lis
        if not self.dp[start_index]:
            self.dp[start_index] = max_lis
        return max_lis
