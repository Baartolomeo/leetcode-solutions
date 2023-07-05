"""Description.

Given n pairs of parentheses, write a function to generate
all combinations of well-formed parentheses.

Example:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

"""


class Solution:

    def generateParenthesis(self, n: int):
        """Implementation of problem solution.

        :param n: number of parenthesses pairs
        :return: array contains parentheses combinations

        """
        generic_bracket = ["()"]
        my_set = set()
        prev_brackets = generic_bracket
        for i in range(1, n):
            my_set.clear()
            for el in prev_brackets:
                for j in range(len(el)):
                    my_set.add(el[:j] + "()" + el[j:])
            prev_brackets = my_set.copy()
        return list(prev_brackets)
