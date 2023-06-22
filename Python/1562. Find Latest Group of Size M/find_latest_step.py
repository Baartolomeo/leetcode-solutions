#Time complexity: O(n)
#Space complexity: O(n)

class Solution:

    def __init__(self):
        self.arr = []
        self.m = 0

    def check(self, l, p, i):
        p_res   = -1
        l_res   = -1
        if l <= p:
            if self.arr[i] >= l and self.arr[i] <= p:
                left = self.arr[i] - l
                right = p - self.arr[i]
                if (left == self.m or right == self.m):
                    return i
                if left > self.m:
                    l_res = self.check(l, self.arr[i] - 1, i - 1)
                if right > self.m:
                    p_res = self.check(self.arr[i] + 1, p, i - 1)
                if l_res or p_res:
                    return p_res if p_res > l_res else l_res
            else:
                l_res = self.check(l, p, i - 1)
                if l_res != -1:
                    return l_res

        return -1

    def findLatestStep(self, arr, m):
        self.arr = arr
        self.m = m
        if m == len(arr):
            return len(arr)
        res = self.check(1, len(arr), len(arr) - 1)
        return res
