"""Description:
You are given an integer n representing the number of houses on a number line, numbered from 0 to n - 1.
Additionally, you are given a 2D integer array offers where offers[i] = [starti, endi, goldi],
indicating that ith buyer wants to buy all the houses from starti to endi for goldi amount of gold.

As a salesman, your goal is to maximize your earnings by strategically selecting and selling houses to buyers.
Return the maximum amount of gold you can earn.
Note that different buyers can't buy the same house, and some houses may remain unsold.

Example:
    Input: n = 5, offers = [[0,0,1],[0,2,2],[1,3,2]]
    Output: 3
    Explanation: There are 5 houses numbered from 0 to 4 and there are 3 purchase offers.
    We sell houses in the range [0,0] to 1st buyer for 1 gold and houses in the range [1,3] to 3rd buyer for 2 golds.
    It can be proven that 3 is the maximum amount of gold we can achieve.

"""


class Solution:

    def maximizeTheProfit(self, n, offers) -> int:
        """Implementation of problem solution.

            :param n: number of houses on a number line
            :param offers: 2D array with sale offers where single offer contain:
                    * start - number of first house
                    * end - number of last house
                    * profit - offer price
            :return: maximum amount of gold you can earn as a salesman
        """
        dp = [0] * n
        sorted_offers = sorted(offers, key=lambda x: x[1])
        start_index = 0
        current_max = 0
        for i in range(n):
            for j in range(start_index, len(sorted_offers)):
                start, end, profit = sorted_offers[j]
                if end <= i:
                    if start - 1 >= 0:
                        current_max = max(current_max, dp[start - 1] + profit)
                    else:
                        current_max = max(current_max, profit)
                else:
                    start_index = j
                    break
            dp[i] = max(current_max, dp[i - 1] if i > 0 else 0)

        return dp[n - 1]
