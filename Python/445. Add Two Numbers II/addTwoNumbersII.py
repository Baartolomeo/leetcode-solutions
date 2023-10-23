from typing import Optional

"""Description.

You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
    Input: 
        l1 = [7,2,4,3],
        l2 = [5,6,4]
    Output: 
        [7,8,0,7]

"""


# Time Complexity: O(m + n)
# Space Complexity: O(m + n)

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_stack = []
        l2_stack = []

        # Build Stack of L1
        current_node = l1
        while current_node is not None:
            l1_stack.append(current_node)
            current_node = current_node.next

        # Build Stack of L2
        current_node = l2
        while current_node is not None:
            l2_stack.append(current_node)
            current_node = current_node.next

        current_node = None
        noTensFromPrevSum = 0
        empty_node = ListNode(val=0)
        while l1_stack or l2_stack or noTensFromPrevSum != 0:

            if l1_stack:
                l1_node = l1_stack.pop()
            else:
                l1_node = empty_node

            if l2_stack:
                l2_node = l2_stack.pop()
            else:
                l2_node = empty_node

            # How many tens are in the sum of l1 + l2
            noTens = (l1_node.val + l2_node.val + noTensFromPrevSum) // 10
            if noTens:
                l1L2Sum = (l1_node.val + l2_node.val + noTensFromPrevSum) - noTens * 10
                noTensFromPrevSum = noTens
            else:
                l1L2Sum = l1_node.val + l2_node.val + noTensFromPrevSum
                noTensFromPrevSum = 0

            new_node = ListNode(val=l1L2Sum)
            new_node.next = current_node
            current_node = new_node

        return current_node
