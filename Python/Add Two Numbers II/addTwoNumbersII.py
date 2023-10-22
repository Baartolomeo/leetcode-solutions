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

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_stack = []
        l2_stack = []

        current_node = l1
        while current_node != None:
            l1_stack.append(current_node)
            current_node = current_node.next

        current_node = l2
        while current_node != None:
            l2_stack.append(current_node)
            current_node = current_node.next

        current_node = None
        prev_rest = 0
        while (l1_stack or l2_stack or prev_rest != 0):
            if l1_stack:
                l1_node = l1_stack.pop()
            else:
                l1_node = ListNode(val=0)
            if l2_stack:
                l2_node = l2_stack.pop()
            else:
                l2_node = ListNode(val=0)
            sum_rest = (l1_node.val + l2_node.val + prev_rest) // 10
            if sum_rest:
                sum_val = (l1_node.val + l2_node.val + prev_rest) - sum_rest * 10
                prev_rest = sum_rest
            else:
                sum_val = l1_node.val + l2_node.val + prev_rest
                prev_rest = 0
            new_node = ListNode(val=sum_val)
            new_node.next = current_node
            current_node = new_node

        return current_node


