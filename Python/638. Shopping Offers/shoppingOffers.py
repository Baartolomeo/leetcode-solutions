"""Description

In LeetCode Store, there are n items to sell. Each item has a price.
However, there are some special offers, and a special offer
consists of one or more different kinds of items with a sale price.

You are given an integer array price where price[i] is the price of the ith item,
and an integer array needs where needs[i] is the number of pieces of the ith item you want to buy.
You are also given an array special where special[i] is of size n + 1 where special[i][j] is the number of pieces
of the jth item in the ith offer and special[i][n] (i.e., the last integer in the array) is the price of the ith offer.

Return the lowest price you have to pay for exactly certain items as given,
where you could make optimal use of the special offers. You are not allowed to buy more items than you want,
even if that would lower the overall price. You could use any of the special offers as many times as you want.

Example:
    Input: price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]
    Output: 14
    Explanation: There are two kinds of items, A and B. Their prices are $2 and $5 respectively.
    In special offer 1, you can pay $5 for 3A and 0B
    In special offer 2, you can pay $10 for 1A and 2B.
    You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.

"""


class Solution:

    def __init__(self):
        self.dp = {}

    def shoppingOffers(self, price, special, needs):
        """Implementation of problem solution.

            :param price: array with prices for items
            :param special: array of special which consist items for a sale price.
            :param needs: array of items to buy
            :return: lowest price.
        """
        cost = self.min_cost(needs, special, price)
        return cost

    def min_cost(self, needs, special, price):
        """Calculates the lowest price for given needs to buy.

            :param price: array with prices for items
            :param special: array of special which consist items for a sale price.
            :param needs: array of items to buy
            :return: lowest price for given needs.
        """
        cost = sum(needs[i] * price[i] for i in range(len(needs)))
        if self.dp.get(tuple(needs)):
            return self.dp[tuple(needs)]

        for spec in special:
            if self.is_valid(needs, spec):
                new_needs = self.get_new_needs(needs, spec)
                cost = min(spec[-1] + self.min_cost(new_needs, special, price), cost)

        self.dp[tuple(needs)] = cost
        return cost

    def _is_valid(self, needs, special):
        """Check if given special can be applied.

            :param needs: array of items to buy
            :param special: array of items for a sale price
            :return: true if special can be applied
        """
        for need, spec in zip(needs, special[:-1]):
            if need < spec:
                return False
        return True

    def _get_new_needs(self, needs, special):
        """Calculate needs after applying special to it.

            :param needs: array of items to buy
            :param special: array of items for a sale price
            :return: needs reduced by special offer.
        """
        new_needs = []
        for need, spec in zip(needs, special[:-1]):
            new_needs.append(need - spec)
        return new_needs
