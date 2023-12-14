"""Description:

Given two strings s and t, find the number of ways you can choose a non-empty substring of s
and replace a single character by a different character such that the resulting substring is a substring of t.
In other words, find the number of substrings in s that differ from some substring in t by exactly one character.

For example, the underlined substrings in "computer" and "computation"
only differ by the 'e'/'a', so this is a valid way.
Return the number of substrings that satisfy the condition above.
A substring is a contiguous sequence of characters within a string.

Example:
    Input:
        s = "aba",
        t = "baba"
    Output: 6
    Explanation: The following are the pairs of substrings from s and t that differ by exactly 1 character:
        ("aba", "baba")
        ("aba", "baba")
        ("aba", "baba")
        ("aba", "baba")
        ("aba", "baba")
        ("aba", "baba")
    The underlined portions are the substrings that are chosen from s and t.

"""

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        """Implementation of problem solution.

            :param s: first string
            :param t: second string
            :return: number of substrings
                     that differ by one character
        """
        s_char_map = {i: {} for i in range(1, len(t) + 1)}
        for i in range(len(s)):
            for j in range(i, len(s)):
                if not s_char_map[len(s[i:j + 1])].get(s[i:j + 1]):
                    s_char_map[len(s[i:j + 1])][s[i:j + 1]] = 1
                else:

                    s_char_map[len(s[i:j + 1])][s[i:j + 1]] += 1

        t_char_map = {i: {} for i in range(1, len(t) + 1)}
        for i in range(len(t)):
            for j in range(i, len(t)):
                if not t_char_map[len(t[i:j + 1])].get(t[i:j + 1]):
                    t_char_map[len(t[i:j + 1])][t[i:j + 1]] = 1
                else:
                    t_char_map[len(t[i:j + 1])][t[i:j + 1]] += 1

        results = 0
        for i in range(1, len(t) + 1):
            for key_s, item_s in s_char_map[i].items():
                for key_t, item_t in t_char_map[i].items():
                    if self.check_differ_by_one_char(key_s, key_t):
                        results += item_s * item_t

        return results

    @staticmethod
    def check_differ_by_one_char(s1: str, s2: str) -> bool:
        """Check if strings s1 and s2 differ by only one char.

            :param s1: first string
            :param s2: second string
            :return: 'true' if differ by only one char

        """
        different_chars_count = 0
        for char_s, char_z in zip(s1, s2):
            if char_s != char_z:
                if different_chars_count == 1:
                    different_chars_count = 2
                    break
                different_chars_count = 1
        return different_chars_count == 1
