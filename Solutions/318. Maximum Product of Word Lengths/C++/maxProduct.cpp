// Time complexity: O(n^3) / O(n^2)
// Space complexity: O(n)

/*Description:

Given a string array words, return the maximum value of length(word[i]) * length(word[j])
where the two words do not share common letters. If no such two words exist, return 0.

Example:
    Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    Output: 16
    Explanation: The two words can be "abcw", "xtfn".
*/

#include <map>
#include <vector>

typedef std::map<char, bool> char_to_bool;

class Solution {
public:
    int maxProduct(vector<string>& words) {
        std::vector<char_to_bool> words_letters_map; 
        for (int i = 0; i < words.size(); i++)
        {
            char_to_bool temp;
            for (int j = 0; j < words[i].length(); j++)
                temp[words[i][j]] = true;
            words_letters_map.push_back(temp);
        }

        int max_val = 0;
        bool words_not_share_letters = false;
        for (int i = 0; i < words.size() - 1; i++)
        {
            for (int j = i + 1; j < words.size(); j++)
            {
                words_not_share_letters = true;

                for (char z = 'a'; z <= 'z'; z++)
                {
                    if (words_letters_map[j][z] && words_letters_map[i][z])
                    {
                        words_not_share_letters = false;
                        break;
                    }
                }

                if (words_not_share_letters == true)
                {
                    int temp_max = words[i].length() * words[j].length();
                    max_val = temp_max > max_val ? temp_max : max_val;
                }
            }
        }

        return max_val;
    }


};