//Time complexity: O(n)
//Space complexity: O(1)

/*Description

Given an binary array nums and an integer k, return true if all 1's are at
least k places away from each other, otherwise return false.

Example:
    Input: nums = [1,0,0,0,1,0,0,1], k = 2
    Output: true
    Explanation: Each of the 1s are at least 2 places away from each other.

*/

class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        int prevIndexWithOne = 0;
        for (int i = 1; nums.size() > i; i++)
        {
            if (nums[i])
            {
                if (1 + nums[prevIndexWithOne] == 2)
                {
                    if (i - 1 - prevIndexWithOne < k)
                    {
                        return false;
                    }
                }
                prevIndexWithOne = i;
            }
        }
        return true;
    }
};