class Solution:

    def generateParenthesis(self, n: int):
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
