//Time complexity: O(N^2)
//Space complexity: O(N)

#include <map>
#include <cstdlib>

class Solution {
public:
    bool isItPossible(string word1, string word2) {

        map < char, int> hm_word1, hm_word2;
        const int max_length = word1.length() > word2.length() ? word1.length() : word2.length();
        for (auto i = 0; i < max_length; i++)
        {
            if (i < word1.length())
            {
                hm_word1[word1[i]] += 1;
            }

            if (i < word2.length())
            {
                hm_word2[word2[i]] += 1;
            }
        }

        int distinct_chars_in_word1, distinct_chars_in_word2;
        const int hm_word1_size = hm_word1.size(), hm_word2_size = hm_word2.size();

        if (abs(hm_word1_size - hm_word2_size) > 2)
            return false;

        for (auto const& i : hm_word1)
        {
            for (auto const& j : hm_word2)
            {
                distinct_chars_in_word1 = hm_word1_size;
                distinct_chars_in_word2 = hm_word2_size;

                if (i.first == j.first && distinct_chars_in_word1 == distinct_chars_in_word2)
                    return true;

                if (i.second == 1)
                    distinct_chars_in_word1--;

                if (!hm_word1.count(j.first) || (i.second==1 && i.first == j.first))
                    distinct_chars_in_word1++;

                if (j.second == 1)
                    distinct_chars_in_word2--;

                if (!hm_word2.count(i.first) || (j.second==1 && i.first == j.first))
                    distinct_chars_in_word2++;

                if (distinct_chars_in_word2 == distinct_chars_in_word1)
                    return true;
            }
        }

        return false;

    }
};