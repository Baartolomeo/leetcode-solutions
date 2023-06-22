#Time complexity: O(n^2)
#Space complexity: O(n^2)

class Solution:

    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        my_dict = {}
        num_str = ''
        divisible = 0
        for i in range(len(nums)):
            divisible = 0
            num_str = ''
            for j in range(i, len(nums)):
                if not (nums[j] % p):
                    divisible += 1
                    if (divisible > k):
                        break
                num_str += str(nums[j])
                num_str += ';'
                if not (my_dict.get(num_str)):
                    my_dict[num_str] = '1'
        return len(my_dict.keys())
